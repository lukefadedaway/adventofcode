from sys import stdin
import re

def extract_with_indices(input_string, pattern):
    result = [(match.start(), str(match.group())) for match in pattern.finditer(input_string)]
    return result

numbers = []
otherchars = []
solution = []
solution2 = []
for line in stdin:
    numbers.append(extract_with_indices(line.strip(),re.compile(r'\d+')))
    otherchars.append(extract_with_indices(line.strip(),re.compile(r'[^.\d]+')))
numbers2 = [i for i in numbers]
for i in range(len(otherchars)):
    for a in otherchars[i]:
        above = []
        below = []
        along = [(x, s) for x, s in numbers[i] if a[0] == x + len(s) or a[0]+1 == x]
        above2 = []
        below2 = []
        along2 = [(x, s) for x, s in numbers2[i] if a[0] == x + len(s) or a[0]+1 == x]
        numbers[i] = [l for l in numbers[i] if l not in along]
        if i > 0:
            above = [(x, s) for x, s in numbers[i-1] if (x <= a[0] <= x + len(s)) or a[0] == x + len(s) or a[0]+1 == x]
            above2 = [(x, s) for x, s in numbers2[i-1] if (x <= a[0] <= x + len(s)) or a[0] == x + len(s) or a[0]+1 == x]
            numbers[i-1] = [l for l in numbers[i-1] if l not in above]
        if i < len(otherchars)-1:
            below = [(x, s) for x, s in numbers[i+1] if (x <= a[0] <= x + len(s)) or a[0] == x + len(s) or a[0]+1 == x]
            below2 = [(x, s) for x, s in numbers2[i+1] if (x <= a[0] <= x + len(s)) or a[0] == x + len(s) or a[0]+1 == x]
            numbers[i+1] = [l for l in numbers[i+1] if l not in below]
        if(a[1] == '*'):
            parsol2 = above2 + along2 + below2
            if len(parsol2) == 2:
                solution2 += [int(parsol2[0][1]) * int(parsol2[1][1])]
        solution += [int(s) for x,s in above]
        solution += [int(s) for x,s in below]
        solution += [int(s) for x,s in along]
print("Part 1:",sum(solution))
print("Part 2:",sum(solution2))
