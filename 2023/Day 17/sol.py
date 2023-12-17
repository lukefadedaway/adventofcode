from sys import stdin
from heapq import heappop, heappush

lines = [i.strip() for i in stdin.read().splitlines()]
matrix = [[int(i) for i in line] for line in lines]
matrix[0][0] = 0

moves = [(-1, 0), (0, -1), (0, 1), (1, 0)]
movesp = {(-1, 0):"U", (0, -1):"L", (0, 1):"R", (1, 0):"D"}

def checkp(p):
    if len(p) < 3:
        return False
    return p[-1] == p[-2] == p[-3]

def dijk(part1 = True):
    # tuple: (heat-loss, x, y, path, x-dir, y-dir)
    q = [(0, 0, 0, "", 0, 0)]
    visited = set()
    while q:
        loss, x, y, p, dx, dy = heappop(q)
        if x == len(matrix)-1 and y == len(matrix[0])-1:
            if not part1 and len(p) < 4:
                continue
            break
        if part1:
            if any((x,y,k,dx,dy) in visited for k in range(1,len(p)+1)):
                continue
        else:
            if (x, y, len(p), dx, dy) in visited:
                continue
        visited.add((x, y,len(p), dx, dy))
        for new_dx, new_dy in moves:
            straight = (len(p) == 0 or p[-1] == movesp[(new_dx,new_dy)])
            new_x, new_y = x + new_dx, y + new_dy
            if part1:
                if any((new_dx == -dx and new_dy == -dy,
                        checkp(p) and straight,
                        new_x < 0, new_y < 0,
                        new_x == len(matrix), new_y == len(matrix[0]))):
                    continue
            else:
                if any((new_dx == -dx and new_dy == -dy,
                    len(p) == 10 and straight,
                    len(p) < 4 and not straight,
                    new_x < 0, new_y < 0,
                    new_x == len(matrix), new_y == len(matrix[0]))):
                    continue
            #new_p = p + movesp[(new_dx,new_dy)]
            if len(p):
                new_p = p + p[-1] if straight else movesp[(new_dx,new_dy)]
            else:
                new_p = movesp[(new_dx,new_dy)]
            heappush(q, (loss + matrix[new_x][new_y], new_x, new_y, new_p, new_dx, new_dy))
    return loss

solution = dijk()
solution2 = dijk(False)
print("Part 1:", solution)
print("Part 2:", solution2)
