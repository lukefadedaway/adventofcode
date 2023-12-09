from sys import stdin

lines = [i.strip() for i in stdin.read().splitlines()]

solution = []
solution2 = []
for line in lines:
    current = [[int(i) for i in line.split(' ')]]
    difference = [current[-1][i]-current[-1][i-1] for i in range(1,len(current[-1]),1)]
    while not set(difference) == set([0]):
        current.append(difference)
        difference = [current[-1][i]-current[-1][i-1] for i in range(1,len(current[-1]),1)]
    current.append(difference)
    for i in range(len(current)-1,0,-1):
        current[i-1].append(current[i-1][-1]+current[i][-1])
        current[i-1] = [current[i-1][0]-current[i][0]] + current[i-1]
    solution.append(current[0][-1])
    solution2.append(current[0][0])
print("Part 1:",sum(solution))
print("Part 2:",sum(solution2))
