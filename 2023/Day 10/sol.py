from sys import stdin

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
print("Part 1:",counter // 2)
#print("Part 2:",401)
