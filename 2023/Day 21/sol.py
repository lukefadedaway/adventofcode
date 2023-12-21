from sys import stdin
from queue import Queue

lines = ["#"+i.strip()+"#" for i in stdin.read().splitlines()]
lines = ['#' * len(lines[1])] + lines + ['#' * len(lines[1])]

visited = [[set() for c in line] for line in lines]
spos = [0,0]
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == 'S':
            spos = [i,j]
q = Queue()
q.put((spos[0],spos[1],1))
run = True
while run and q.qsize():
    x,y,p = q.get()
    if p < 132:
        for n in [[0,1],[0,-1],[1,0],[-1,0]]:
            x1 = x+n[0]
            y1 = y+n[1]
            if not lines[x1][y1] == '#' and len(visited[x1][y1]) == 0:
                visited[x1][y1].add(p)
                q.put((x1,y1,p+1))
    if p > 131:
        run = False
solution = 0
alleven = allodd = cornereven = cornerodd = 0
for v in visited:
    for vv in v:
        ad = 0
        for vvv in vv:
            if vvv % 2 == 0:
                if vvv < 65:
                    ad = 1
                alleven += 1
                if vvv > 65:
                    cornereven += 1
            else:
                allodd += 1
                if vvv > 65:
                    cornerodd += 1
        solution += ad
n = 202300
# print(alleven, allodd, cornereven, cornerodd) -- Werden falsch gezählt
solution2 = (n*n) * allodd + ((n + 1) * (n + 1)) * alleven - ((n + 1) * cornerodd) + (n * cornereven) # https://github.com/villuna/aoc23/wiki/A-Geometric-solution-to-advent-of-code-2023,-day-21
print("Part 1:", solution)
#print("Part 2:",solution2) # 609298746763952
