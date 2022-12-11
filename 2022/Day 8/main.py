# Array of rows
import math

forest = []
s = input()
length = len(s)
forest.append(s)
forestvis = []
forestscore = []
forestvis.append([False for _ in range(length)])
forestscore.append([[0,0,0,0] for _ in range(length)])
for _ in range(1,len(s)):
    s = input()
    forest.append(s)
    forestvis.append([False for _ in range(length)])
    forestscore.append([[0,0,0,0] for _ in range(length)])
    
# -> && ↑ 
for x in range(0,length):
    minimum = -1
    minimum2 = -1
    for y in range(0,length):
        if(int(forest[x][y]) > minimum):
            forestvis[x][y] = True
            minimum = int(forest[x][y])
        if(int(forest[y][x]) > minimum2):
            forestvis[y][x] = True
            minimum2 = int(forest[y][x])

# <- && ↓ 
for x in range(length-1, -1, -1):
    minimum = -1
    minimum2 = -1
    for y in range(length-1, -1, -1):
        if(int(forest[x][y]) > minimum):
            forestvis[x][y] = True
            minimum = int(forest[x][y])
        if(int(forest[y][x]) > minimum2):
            forestvis[y][x] = True
            minimum2 = int(forest[y][x])           

for x in range(0,length):
    for y in range(0,length):
        for z in range(x-1,-1,-1):
            if(int(forest[x][y]) > int(forest[z][y])):
                forestscore[x][y][0] += 1
            else:
                forestscore[x][y][0] += 1
                break
        for z in range(x+1,length):
            if(int(forest[x][y]) > int(forest[z][y])):
                forestscore[x][y][1] += 1
            else:
                forestscore[x][y][1] += 1
                break
        for z in range(y-1,-1,-1):
            if(int(forest[x][y]) > int(forest[x][z])):
                forestscore[x][y][2] += 1
            else:
                forestscore[x][y][2] += 1
                break
        for z in range(y+1,length):
            if(int(forest[x][y]) > int(forest[x][z])):
                forestscore[x][y][3] += 1
            else:
                forestscore[x][y][3] += 1
                break
        

part2 = 0
for x in range(0,length):
    for y in range(0,length):
        part2 = max(part2, math.prod(forestscore[x][y]))
        #print(forest[x][y],forestscore[x][y])

part1 = 0
for x in range(0,length):
    for y in range(0,length):
        if forestvis[x][y]:
            part1 += 1

print("Part 1:")
print(part1)
print("Part 2:")
print(part2)
