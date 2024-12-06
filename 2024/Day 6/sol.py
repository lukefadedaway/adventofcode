from sys import stdin
import re

def checkInf(grid, point, start):
    taken = set()
    directions = [(-1,0),(0,1),(1,0),(0,-1)]
    direction = 0
    slist = list(grid[point[0]])
    slist[point[1]] = "#"
    grid[point[0]] = ''.join(slist)
    while start[0] > -1 and start[0] <= len(grid[0]) and start[1] > -1 and start[1] <= len(grid):
        slist = list(grid[start[0]])
        slist[start[1]] = "S"
        grid[start[0]] = ''.join(slist)
        if (tuple(start), direction) in taken:
            #slist = list(grid[point[0]])
            #slist[point[1]] = "O"
            #grid[point[0]] = ''.join(slist)
            #print("\n".join(grid),"\n")
            #print(taken, "\n\n", (tuple(start), direction))
            return 1
        taken.add((tuple(start), direction))
        nextposition = [0,0]
        nextposition[0] = start[0] + directions[direction][0]
        nextposition[1] = start[1] + directions[direction][1]
        if nextposition[0] < -1 or nextposition[0] >= len(grid[0]) or nextposition[1] < -1 or nextposition[1] >= len(grid):
            break
        valid = True
        if grid[nextposition[0]][nextposition[1]] == "#" or point == (nextposition[0],nextposition[1]):
            valid = False
        while not valid:
            direction = (direction + 1) % 4
            nextposition[0] = start[0] + directions[direction][0]
            nextposition[1] = start[1] + directions[direction][1]
            if nextposition[0] < -1 or nextposition[0] >= len(grid[0]) or nextposition[1] < -1 or nextposition[1] >= len(grid):
                break
            valid = True
            if grid[nextposition[0]][nextposition[1]] == "#" or point == (nextposition[0],nextposition[1]):
                valid = False
        taken.add((tuple(start), direction))
        start = nextposition
    return 0

sol1 = 0
sol2 = 0
directions = [(-1,0),(0,1),(1,0),(0,-1)]
lines = []
position = [0,-1]
direction = 0
path = set()
for line in stdin:
    if '^' in line:
        position[1] = line.index("^")
    else:
        if position[1] == -1:
            position[0] += 1
    lines.append(line.strip())
startposition = [x for x in position]
while position[0] > -1 and position[0] <= len(lines[0]) and position[1] > -1 and position[1] <= len(lines):
    slist = list(lines[position[0]])
    slist[position[1]] = "X"
    lines[position[0]] = ''.join(slist)
    nextposition = [0,0]
    nextposition[0] = position[0] + directions[direction][0]
    nextposition[1] = position[1] + directions[direction][1]
    if nextposition[0] < -1 or nextposition[0] >= len(lines[0]) or nextposition[1] < -1 or nextposition[1] >= len(lines):
        break
    valid = True
    if lines[nextposition[0]][nextposition[1]] == "#":
        valid = False
    while not valid:
        direction = (direction + 1) % 4
        nextposition[0] = position[0] + directions[direction][0]
        nextposition[1] = position[1] + directions[direction][1]
        if nextposition[0] < -1 or nextposition[0] >= len(lines[0]) or nextposition[1] < -1 or nextposition[1] >= len(lines):
            break
        valid = True
        if lines[nextposition[0]][nextposition[1]] == "#":
            valid = False
    position = nextposition
    path.add((tuple(position), direction))
for line in lines:
    sol1 += line.count("X")
npath = set()
for x, _ in path:
    npath.add(x) 
for x in npath:
    sol2 += checkInf(lines.copy(), list(x), startposition.copy())
print(sol1)
# Too high, 1907 > 1888
print(sol2)