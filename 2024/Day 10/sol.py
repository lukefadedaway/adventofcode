from sys import stdin
import re
from itertools import combinations

nines = []
def getS(lines, position, score):
    global nines 
    nines = []
    if lines[position[0]][position[1]] != 0:
        return 0
    return score + sum([getScore(lines, s, position, score) for s in [[position[0], position[1] + 1], [position[0], position[1] - 1], [position[0] + 1, position[1]], [position[0] - 1, position[1]]]])

def getScore(lines, position, last, score):
    global nines 
    if position[0] < 0 or position[0] >= len(lines):
        return 0
    if position[1] < 0 or position[1] >= len(lines[0]):
        return 0
    if lines[position[0]][position[1]] != (lines[last[0]][last[1]] + 1):
        return 0
    if lines[position[0]][position[1]] == 9:
        nines += [(position[0],position[1])]
        return 1
    return score + sum([getScore(lines, s, position, score) for s in [[position[0], position[1] + 1], [position[0], position[1] - 1], [position[0] + 1, position[1]], [position[0] - 1, position[1]]]])
    
sol1 = 0
sol2 = 0
lines = []

for line in stdin:
    lines.append([int(x) for x in line.strip()])
for i in range(len(lines)):
    for j in range(len(lines[i])):
        sol2 += getS(lines, [i,j], 0)
        sol1 += len(set(nines))
print(sol1)
print(sol2)