from sys import stdin
import re
from itertools import combinations

sol1 = 0
sol2 = 0
lines = []

for line in stdin:
    lines.append([int(x) for x in line.strip().split()])

print(sol1)
print(sol2)