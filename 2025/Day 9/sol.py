from sys import stdin
from collections import defaultdict

points = [
    tuple(map(int, line.strip().split(',')))
    for line in stdin
]
group_x = defaultdict(list)
group_y = defaultdict(list)
for x, y in points:
    group_x[x].append(y)
    group_y[y].append(x)

vert = []
horiz = []
for x, ys in group_x.items():
    yss = sorted(ys)
    for i in range(len(yss) // 2):
        a = (x, yss[2 * i])
        b = (x, yss[2 * i + 1])
        vert.append((a, b))
for y, xs in group_y.items():
    xss = sorted(xs)
    for i in range(len(xss) // 2):
        a = (xss[2 * i], y)
        b = (xss[2 * i + 1], y)
        horiz.append((a, b))

sol1 = 0
sol2 = 0

for i in range(len(points)):
    #print((i/(len(points)-1))*100, "%")
    for j in range(i+1, len(points)):
        sol1 = max(sol1, (abs(points[j][0]-points[i][0])+1)*(abs(points[j][1]-points[i][1])+1))
        
        minx = min(points[i][0], points[j][0])
        maxx = max(points[i][0], points[j][0])
        miny = min(points[i][1], points[j][1])
        maxy = max(points[i][1], points[j][1])
        yes2 = True
        for p, q in vert:
            x = p[0]
            y1 = min(p[1], q[1])
            y2 = max(p[1], q[1])
            if x > minx and x < maxx:
                if not (y2 <= miny or y1 >= maxy):
                    yes2 = False
                    break
        if yes2:
            for p, q in horiz:
                y = p[1]
                x1 = min(p[0], q[0])
                x2 = max(p[0], q[0])
                if y > miny and y < maxy:
                    if not (x2 <= minx or x1 >= maxx):
                        yes2 = False
                        break
        if yes2:
            sol2 = max(sol2, (abs(points[j][0]-points[i][0])+1)*(abs(points[j][1]-points[i][1])+1))
print(sol1)
print(sol2)