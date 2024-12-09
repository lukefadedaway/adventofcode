from sys import stdin
import re
from itertools import combinations

sol1 = 0
sol2 = 0
fs = []
fs2 = []
for line in stdin:
    x = line.strip()
    counter = 0
    for i in range(len(x)):
        if i % 2 == 0:
            fs += [counter for _ in range(int(x[i]))]
            fs2.append((counter, int(x[i])))
            counter += 1
        else:
            fs += [-1 for _ in range(int(x[i]))]
            if int(x[i]) > 0:
                fs2.append((-1, int(x[i])))
ind = len(fs)-1
ind1 = fs.index(-1)
while ind >= ind1:
    fs[ind1] = fs[ind]
    fs[ind] = -1
    ind -= 1
    ind1 = fs.index(-1)
fs2.reverse()
i = 0
while i < len(fs2):
    j = i
    while j < len(fs2)-1:
        if fs2[j][0] == fs2[j+1][0]:
            fs2 = fs2[:j] + [(fs2[j][0], fs2[j][0]+fs2[j][1])] + fs2[j+2:]
        j+= 1
    if fs2[i][0] == -1:
        i += 1
        continue
    else:
        i2 = len(fs2) - 1
        while i2 >= i:
            if fs2[i2][0] == -1:
                if fs2[i2][1] == fs2[i][1]:
                    fs2[i2] = fs2[i]
                    fs2[i] = (-1, fs2[i][1])
                    i2 = -1
                    i += 1
                elif fs2[i2][1] > fs2[i][1]:
                    fs2 = fs2[:i2] + [(-1, fs2[i2][1] - fs2[i][1])] + [fs2[i]] + fs2[i2+1:]
                    fs2[i] = (-1, fs2[i][1])
                    i2 = -1
                    i += 1
            i2 -= 1
        i += 1
fs2.reverse()
fs1 = []
for i in range(len(fs2)):
    fs1 += [fs2[i][0] for _ in range(fs2[i][1])]
for i in range(len(fs)):
    if fs[i] != -1:
        sol1 += (fs[i] * i)
    if fs1[i] != -1:
        sol2 += (fs1[i] * i)
print(sol1)
# Too high 6781700067558
print(sol2)