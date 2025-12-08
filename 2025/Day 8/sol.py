from sys import stdin 
from math import sqrt

points = [
    tuple(map(int, line.strip().split(',')))
    for line in stdin
]
circs = [[i] for i in range(len(points))]
distances = []
for i in range(len(points)):
    for j in range(i+1, len(points)):
        dist = sqrt(((points[i][0]-points[j][0])**2)+((points[i][1]-points[j][1])**2)+((points[i][2]-points[j][2])**2))
        distances.append((i,j,dist))
distances.sort(key=lambda t: t[2])
newconnect = 0
for i in distances:
    if newconnect == 1000:
        print(len(circs[0])*len(circs[1])*len(circs[2]))
    newconnect += 1
    a = next((x for x, sub in enumerate(circs) if i[0] in sub), -1)
    b = next((x for x, sub in enumerate(circs) if i[1] in sub), -1)
    if a == b and a > -1:
        continue
    if a == -1 and b == -1:
        circs.append([i[0],i[1]])
    elif a == -1 and b > -1:
        circs[b].append(i[0])
    elif a > -1 and b == -1:
        circs[a].append(i[1])
    else:
        circs[a] += circs[b]
        circs[b] = []
    circs = sorted((x for x in circs if x), key=len, reverse=True)
    if len(circs) == 1:
        print(points[i[0]][0] * points[i[1]][0])
        break
