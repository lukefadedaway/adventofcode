from sys import stdin
import re

sol1 = 0
sol2 = 0
pattern = r"mul\(\d+,\d+\)"
pattern2 = r"(mul\(\d+,\d+\)|do\(\)|don't\(\))"
lines = ""
for line in stdin:
    lines += line.strip()
    matches = re.findall(pattern, line)
    l = [x.replace('mul(', '').replace(')', '') for x in matches]
    sol1 += sum([int(x[0])*int(x[1]) for x in [a.split(',') for a in l]])
matches = re.findall(pattern2, lines)
res = []
do = True
for i in range(len(matches)):
    if matches[i][0] == 'm' and do:
        res += [matches[i]]
    if matches[i][2] == "(":
        do = True
    if matches[i][2] == "n":
        do = False
l = [x.replace('mul(', '').replace(')', '') for x in res]
sol2 += sum([int(x[0])*int(x[1]) for x in [a.split(',') for a in l]])
print(sol1)
print(sol2)