from sys import stdin
import re
from itertools import combinations

sol1 = 0
sol2 = 0
lines = []
sto = {}
sto25 = {}

for line in stdin:
    lines.append([int(x) for x in line.strip().split()])
stones = lines[0]

for j in range(25):
    for i in range(len(stones)):
        if stones[i] == 0:
            stones[i] = 1
            continue
        if len(str(stones[i])) % 2 == 0:
            s = str(stones[i])
            stones[i] = int(s[:len(s)//2])
            stones += [int(s[len(s)//2:])]
            continue
        stones[i] *= 2024
sol1 = len(stones)
print(sol1)
for o in stones:
    if o in sto.keys():
        sto[o] += 1
    else:
        sto[o] = 1
for j in range(50):
    sto2 = {}
    for o in sto.keys():
        if o == 0:
            sto2[1] += sto[o]
            sto[o] = 0
            continue
        elif len(str(o)) % 2 == 0:
            s = str(o)
            half1 = int(s[:len(s)//2])
            half2 = int(s[len(s)//2:])
            if half1 in sto2:
                sto2[half1] += sto[o]
            else:
                sto2[half1] = sto[o]
            if half2 in sto2:
                sto2[half2] += sto[o]
            else:
                sto2[half2] = sto[o]
            sto[o] = 0
            continue
        else:
            if (o*2024) in sto2:
                sto2[o*2024] += sto[o]
            else:
                sto2[o*2024] = sto[o]
            sto[o] = 0
    for o in sto2.keys():
        sto[o] = sto2[o]
for o in sto:
    sol2 += sto[o]
print(sol2)