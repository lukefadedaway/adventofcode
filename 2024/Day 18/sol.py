from sys import stdin
import re
from itertools import combinations
import math
import networkx as nx

sol1 = 0
sol2 = "0"
lines = []
grid = [['.' for _ in range(71)] for _ in range(71)]

for line in stdin:
    lines.append(line.strip())
    a, b = [int(x) for x in lines[-1].split(",")]
    if len(lines) < 1024:
        grid[b][a] = '#'
g = nx.DiGraph()
for i in range(70):
    for j in range(70):
        for d in [(0,1), (1,0)]:
            if grid[i][j] == '#' or grid[i+d[0]][j+d[1]] == '#':
                continue
            g.add_edge((i,j),(i+d[0],j+d[1]), weight=1)
            g.add_edge((i+d[0],j+d[1]), (i,j), weight=1)
for i in range(70):
    if grid[i][70] == '.' and grid[i+1][70] == '.':
        g.add_edge((i,70), (i+1,70), weight=1)
    if grid[70][i+1] == '.' and grid[70][i] == '.':
        g.add_edge((70,i), (70,i+1), weight=1)
#for i in range(len(grid)):
#    print(''.join(grid[i]))
path = nx.shortest_path(g, (0, 0), (70, 70), "weight")
for i in range(len(path)-1):
    sol1 += g.edges[(path[i], path[i+1])]["weight"]
for o in range(1024, len(lines)):
    a, b = [int(x) for x in lines[o].split(",")]
    grid[b][a] = '#'
    """
    if a == 36 and b == 17 or a == 17 and b == 36:
        print(i)
    for d in [(0,1), (1,0), (-1,0), (0,-1)]:
        try:
            g.remove_edge((a,b),(a+d[0],b+d[1]))
        except:
            sol2 = "0"
        try:
            g.remove_edge((a+d[0],b+d[1]),(a,b))
        except:
            sol2 = "0"
    """
    g = nx.DiGraph()
    for i in range(70):
        for j in range(70):
            for d in [(0,1), (1,0)]:
                if grid[i][j] == '#' or grid[i+d[0]][j+d[1]] == '#':
                    continue
                g.add_edge((i,j),(i+d[0],j+d[1]), weight=1)
                g.add_edge((i+d[0],j+d[1]), (i,j), weight=1)
    for i in range(70):
        if grid[i][70] == '.' and grid[i+1][70] == '.':
            g.add_edge((i,70), (i+1,70), weight=1)
        if grid[70][i+1] == '.' and grid[70][i] == '.':
            g.add_edge((70,i), (70,i+1), weight=1)
    if not nx.has_path(g, (0, 0), (70, 70)):
        sol2 = lines[o]
        break

print(sol1)
print(sol2)
