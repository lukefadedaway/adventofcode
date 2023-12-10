from sys import stdin
from PIL import Image, ImageDraw

lines = [i.strip() for i in stdin.read().splitlines()]
start = []
# ±x,±y = -up/+down , -left/+right
movement_directions = {'|':[[1,0],[-1,0]],
                       '-':[[0,1],[0,-1]],
                       'L':[[-1,0],[0,1]],
                       'J':[[-1,0],[0,-1]],
                       '7':[[1,0],[0,-1]],
                       'F':[[1,0],[0,1]],
                       '.':[[0,0]]}
drawshapes = {'|':[[False,True,False],[False,True,False],[False,True,False]],
              '-':[[False,False,False],[True,True,True],[False,False,False]],
              'L':[[False,True,False],[False,True,True],[False,False,False]],
              'J':[[False,True,False],[True,True,False],[False,False,False]],
              '7':[[False,False,False],[True,True,False],[False,True,False]],
              'F':[[False,False,False],[False,True,True],[False,True,False]]}
visited = [[False for _ in range(len(lines[0]))] for _ in range(len(lines))]
sx = sy = 0
def links_back(point,newpoint):
    if min(newpoint) < 0:
        return False
    tile = lines[newpoint[0]][newpoint[1]]
    if tile == 'S':
        return True
    tilemove = movement_directions[tile]
    for i in tilemove:
        if [point[0]-newpoint[0],point[1]-newpoint[1]] == i:
            return True
    return False

def getnextmove(point):
    tilemove = movement_directions[lines[point[0]][point[1]]]
    for i in tilemove:
        if point[0]+i[0] >= len(lines) or point[1]+i[1] >= len(lines[0]) or point[0]+i[0] < 0 or point[1]+i[1] < 0 or [point[0]+i[0],point[1]+i[1]] == start:
            continue
        if not visited[point[0]+i[0]][point[1]+i[1]]:
            return [point[0]+i[0],point[1]+i[1]]
    return start

def part2():
    image = Image.new("RGB", (len(visited[0])*3, len(visited)*3), color="white")
    pixels = image.load()

    # Set pixel colors based on the boolean array
    for i in range(len(visited)):
        for j in range(len(visited[0])):
            if not visited[i][j]:
                continue
            shape = lines[i][j]
            for x in range(3):
                for y in range(3):
                    if drawshapes[shape][y][x]:
                        pixels[(j*3+x),(i*3+y)] = (0,0,0)
    ImageDraw.floodfill(image,(0,0), (255,0,0),border=None, thresh=0)
    count_inner = 0
    for i in range(len(visited)):
        for j in range(len(visited[0])):
            colours = [(255,255,255)]
            for x in range(3):
                for y in range(3):
                    colours.append(image.getpixel(((j*3+x),(i*3+y))))
            if len(set(colours)) == 1:
                count_inner += 1
    image.save("output.png")
    return count_inner

for i in range(len(lines)):
    sx = i
    sy = lines[i].find('S')
    if not sy == -1:
        break
start = [sx,sy]
next_moves = [x for x in [[sx+1,sy+0],[sx+0,sy-1],[sx-1,sy+0],[sx+0,sy+1]] if links_back(start,x)]
pos = next_moves[0]
counter = 1
visited[pos[0]][pos[1]] = True
while not lines[pos[0]][pos[1]] == 'S':
    pos = getnextmove(pos)
    counter += 1
    visited[pos[0]][pos[1]] = True
fnext_moves = [[start[0]-x[0],start[1]-x[1]] for x in next_moves]
Sshape = [[False,False,False],[False,True,False],[False,False,False]]
for x in fnext_moves:
    Sshape[1+x[0]][1+x[1]] = True
drawshapes['S'] = Sshape
drawshapes['S'] = [[True,True,True],[True,True,True],[True,True,True]]
print("Part 1:",counter // 2)
print("Part 2:",part2())
