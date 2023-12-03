from sys import stdin
from functools import reduce
from operator import mul

solution = []
solution2 = []
maximumcubes = {"red": 12, "green": 13, "blue": 14}
for line in stdin:
    day = line.split(':')[0].split(' ')[1]
    cubes = line.strip().split(':')[1].split(';')
    possible = True
    maximumcubespart2 = {"red": 0, "green": 0, "blue": 0}
    for cube in cubes:
        for sub in cube.strip().split(','):
            if int(sub.split()[0]) > maximumcubes[sub.split()[1]]:
                possible = False
            maximumcubespart2[sub.split()[1]] = max(maximumcubespart2[sub.split()[1]], int(sub.split()[0]))
                #break
        #if not possible:
        #    break #-- commented to make Part 2
    if possible:
        solution.append(int(day))
    solution2.append(reduce(mul, maximumcubespart2.values(), 1))
print("Part 1:", sum(solution))
print("Part 2:", sum(solution2))
