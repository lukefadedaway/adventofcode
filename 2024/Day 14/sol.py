from sys import stdin
import re
from itertools import combinations
import math

sol1 = 0
sol2 = 0
lines = []
wide = 101#11
tall = 103#7
brett = [[0 for _ in range(tall)] for _ in range(wide)]

for line in stdin:
    lines.append(line.strip())
    e = line.strip().split(" ")
    a = e[0].split("=")[1].split(",")
    b = e[1].split("=")[1].split(",")
    x = (int(b[0]) * 100 + int(a[0])) % wide
    y = (int(b[1]) * 100 + int(a[1])) % tall
    brett[x][y] += 1

sol1 = sum([sum(brett[i][:len(brett[i])//2]) for i in range(len(brett) // 2)])
#for l in [brett[i][:len(brett[i])//2] for i in range(len(brett) // 2)]:
#    print(*l)
brett = list(zip(*brett[::-1]))
for _ in range(3):
    sol1 *= sum([sum(brett[i][:len(brett[i])//2]) for i in range(len(brett) // 2)])
    #print()
    #for l in [brett[i][:len(brett[i])//2] for i in range(len(brett) // 2)]:
    #    print(*l)
    brett = list(zip(*brett[::-1]))

found = False
i = -1
while not found:
    i += 1
    brett2 = [["." for _ in range(tall)] for _ in range(wide)]
    for line in lines:
        e = line.strip().split(" ")
        a = e[0].split("=")[1].split(",")
        b = e[1].split("=")[1].split(",")
        x = (int(b[0]) * i + int(a[0])) % wide
        y = (int(b[1]) * i + int(a[1])) % tall
        brett2[x][y] = "#"
    for l in brett2:
        if ("#"*20) in ''.join(l):
            print()
            print(i)
            for l in [brett2[i] for i in range(len(brett2))]:
                print(*l)
            found = True

print(sol1)
print(sol2)
