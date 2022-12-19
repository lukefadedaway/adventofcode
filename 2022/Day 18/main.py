import sys
import math

lines_ = [line.strip().split(',') for line in sys.stdin]
lines = [(int(line[0]),int(line[1]),int(line[2])) for line in lines_]
minx = 1000
miny = 1000
minz = 1000
maxx = -1
maxy = -1
maxz = -1
for (x,y,z) in lines:
    minx = min(minx,x)
    miny = min(miny,y)
    minz = min(minz,z)
    maxx = max(maxx,x)
    maxy = max(maxy,y)
    maxz = max(maxz,z)

maxd = max(max(maxx,maxy),maxz) + 3
playarea = [[[False for _ in range(maxd)] for _ in range(maxd)] for _ in range(maxd)]

for (x,y,z) in lines:
    playarea[x+1][y+1][z+1] = True

exposedSides = 0

for x in range(1, maxd-1):
    for y in range(1, maxd-1):
        for z in range(1, maxd-1):
            exposedSides += ((1 - playarea[x][y][z+1]) * playarea[x][y][z])
            exposedSides += ((1 - playarea[x][y+1][z]) * playarea[x][y][z])
            exposedSides += ((1 - playarea[x+1][y][z]) * playarea[x][y][z])
            exposedSides += ((1 - playarea[x][y][z-1]) * playarea[x][y][z])
            exposedSides += ((1 - playarea[x][y-1][z]) * playarea[x][y][z])
            exposedSides += ((1 - playarea[x-1][y][z]) * playarea[x][y][z])
print("Part 1:\n",exposedSides)