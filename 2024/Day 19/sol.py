from sys import stdin
import re
from itertools import combinations
import math
import networkx as nx

sol1 = 0
sol2 = 0
lines = []

for line in stdin:
    lines.append(line.strip())
t = lines[0].split(", ")
for i in range(len(lines)-2):
    lookup = [1] + [0] * len(lines[i+2])
    for j in range(len(lines[i+2])):
        for p in t:
            if lines[i+2][j:].startswith(p):
                lookup[j+len(p)] += lookup[j]
    if lookup[-1] > 0:
        sol1 += 1
    sol2 += lookup[-1]
print(sol1)
print(sol2)
