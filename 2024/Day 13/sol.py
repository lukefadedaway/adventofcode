from sys import stdin
import re
from itertools import combinations

sol1 = 0
sol2 = 0
lines = []

for line in stdin:
    lines.append(line.strip())

i = 0
pattern = r"X\+(\d+),\s*Y\+(\d+)"
pattern2 = r"X=(\d+),\s*Y=(\d+)"
while i < len(lines):
    match = re.search(pattern, lines[i])
    if match:
        x1, y1 = map(int, match.groups())
    match = re.search(pattern, lines[i+1])
    if match:
        x2, y2 = map(int, match.groups())
    match = re.search(pattern2, lines[i+2])
    if match:
        x3, y3 = map(int, match.groups())
    i += 4
    a = (x3 * (x2 - y2) - x2 * (x3 - y3)) / (x1 * (x2 - y2) + x2 * (y1 - x1))
    b = (x3 - x1 * a) / x2
    
    if (a == int(a) and b == int(b)):
        sol1 += a * 3 + b;
    
    x3 += 10000000000000
    y3 += 10000000000000
    a = (x3 * (x2 - y2) - x2 * (x3 - y3)) / (x1 * (x2 - y2) + x2 * (y1 - x1))
    b = (x3 - x1 * a) / x2
    
    if (a == int(a) and b == int(b)):
        sol2 += a * 3 + b;

print(int(sol1))
print(int(sol2))
