from sys import stdin

left = []
right = []
solution = []
solution2 = []
for line in stdin:
    x = line.split()
    left.append(int(x[0]))
    right.append(int(x[1]))
left.sort()
right.sort()
for x in range(len(left)):
    solution.append(abs(left[x]-right[x]))
    solution2.append(right.count(left[x])*left[x])
print(sum(solution))
print(sum(solution2))