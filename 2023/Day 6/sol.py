from sys import stdin
from functools import reduce
from operator import mul
import re

lines = stdin.read().splitlines()
time = [int(match) for match in re.findall(r'\d+', lines[0])]
distance = [int(match) for match in re.findall(r'\d+', lines[1])]
time.append(int(''.join([str(i) for i in time])))
distance.append(int(''.join([str(i) for i in distance])))

solution = []
for i in range(len(distance)):
    partsol = 0
    for j in range(time[i]+1):
        if (time[i]-j)*(j) > distance[i]:
            partsol += 1
    if partsol > 0:
        solution.append(partsol)
print("Part 1:",reduce(mul, solution[:-1], 1))
print("Part 2:",solution[-1])
