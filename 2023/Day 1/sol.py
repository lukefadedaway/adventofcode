from sys import stdin

substrings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def find_lowest_index_substring(input_string):
    lowest_index = float('inf')
    lowest_substring = ""

    for substring in substrings:
        index = input_string.find(substring)
        if index != -1 and index < lowest_index:
            lowest_index = index
            lowest_substring = substring

    if lowest_index == float('inf'):
        return (-1, -1)
    else:
        return (lowest_index, lowest_substring)

def find_highest_index_substring(input_string):
    highest_index = float('-inf')
    highest_substring = ""

    for substring in substrings:
        index = input_string.rfind(substring)
        if index != -1 and index > highest_index:
            highest_index = index
            highest_substring = substring

    if highest_index == float('-inf'):
        return (-1, -1)
    else:
        return (highest_index, highest_substring)

solution = []
solution2 = []
for line in stdin:
    numbers = ''.join((ch if ch in '0123456789' else '') for ch in line)
    solution.append(int(numbers[0]+numbers[-1]))
    lower = find_lowest_index_substring(line[:line.find(numbers[0])+1])
    higher = find_highest_index_substring(line[line.rfind(numbers[-1])+1:])
    x1 = str(substrings.index(lower[1])+1) if lower[0] != -1 else numbers[0]
    x2 = str(substrings.index(higher[1])+1) if higher[0] != -1 else numbers[-1]
    solution2.append(int(x1+x2))
    
print("Part 1:",sum(solution))
print("Part 2:",sum(solution2))
