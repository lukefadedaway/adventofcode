# pypy3 main.py < input.txt
import sys, math
lines_ = [line.strip().split("=") for line in sys.stdin]
sensors = sorted([(int(x[1].split(",")[0]),int(x[2].split(":")[0]),int(x[3].split(",")[0]),int(x[4])) for x in lines_])

def dist(x,y,bx,by):
    return abs(x-bx) + abs(y-by)
y=2000000
spots = 0
for x in range(-1000000, 6000000):
    for sx, sy, bx, by in sensors:
        if dist(sx, sy, bx, by) >= dist(sx, sy, x, y) and (bx != x or by != y):
            spots += 1
            break
print("Part 1:")
print(spots)
for y in range(4000001):
    x = 0
    for sx, sy, bx, by in sensors:
        if dist(sx, sy, bx, by) >= dist(sx, sy, x, y):
            x = sx + dist(sx, sy, bx, by) - abs(sy - y) + 1
    if x <= 4000000:
        print("Part 2:")
        print(x * 4000000 + y)