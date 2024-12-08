from sys import stdin
import re
from itertools import combinations

sol1 = 0
sol2 = 0
lines = []
pos = set()
pos2 = set()
apos = set()
antenna = {}
for line in stdin:
    for i in range(len(line.strip())):
        x = line[i]
        if x != '.':
            if x not in antenna:
                antenna[x] = []
            antenna[x].append((len(lines),i))
            apos.add((len(lines),i, x))
    lines.append(line.strip())
for x in antenna:
    for a, b in combinations(antenna[x],2):
        diffx = a[0] - b[0]
        diffy = a[1] - b[1]
        run = 1
        allowed = True
        countl = 0
        while allowed or countl < len(lines):
            countl += 1
            x1 = a[0] + (diffx * run)
            x2 = a[0] - (diffx * run)
            x3 = b[0] + (diffx * run)
            x4 = b[0] - (diffx * run)
            y1 = a[1] + (diffy * run)
            y2 = a[1] - (diffy * run)
            y3 = b[1] + (diffy * run)
            y4 = b[1] - (diffy * run)
            if run == 1:
                pos.add((x1, y1, x))
                pos.add((x2, y2, x))
                pos.add((x3, y3, x))
                pos.add((x4, y4, x))
            pos2.add((x1, y1, x))
            pos2.add((x2, y2, x))
            pos2.add((x3, y3, x))
            pos2.add((x4, y4, x))
            run += 1
            if x1 < 0 or x2 < 0 or x3 < 0 or x4 < 0:
                allowed = False
            if y1 < 0 or y2 < 0 or y3 < 0 or y4 < 0:
                allowed = False
            if x1 >= len(lines) or x2 >= len(lines) or x3 >= len(lines) or x4 >= len(lines):
                allowed = False
            if y1 >= len(lines[0]) or y2 >= len(lines[0]) or y3 >= len(lines[0]) or y4 >= len(lines[0]):
                allowed = False
for x in pos:
    if x not in apos:
        if x[0] >= 0 and x[0] < len(lines) and x[1] >= 0 and x[1] < len(lines[x[0]]):
            a = list(lines[x[0]])
            a[x[1]] = "#"
            lines[x[0]] = ''.join(a)
for x in lines:
    sol1 += x.count('#')
for x in pos2:
    if x[0] >= 0 and x[0] < len(lines) and x[1] >= 0 and x[1] < len(lines[x[0]]):
        a = list(lines[x[0]])
        a[x[1]] = "#"
        lines[x[0]] = ''.join(a)
for x in lines:
    sol2 += x.count('#')
print(sol1)
print(sol2)