from sys import stdin
import re
from itertools import combinations
import math
import networkx as nx

sol1 = 0
sol2 = 0
lines = []
grid = {}
E = 0
S = 0
for line in stdin:
    lines.append(line.strip())
    for x, c in enumerate(lines[-1]):
        grid[(x,len(lines)-1)] = c
        if c == 'E':
            E = (x,len(lines)-1)
        if c == 'S':
            S = (x,len(lines)-1)
g = nx.DiGraph()
for c in grid:
    for d in [(1,0), (-1,0), (0,1), (0,-1)]:
        g.add_edge((c,d), (c,(0,0)), weight=0)
        g.add_edge((c,(0,0)), (c,d), weight=1000)
        a = c[0] + d[0]
        b = c[1] + d[1]
        if grid[c] != '#' and grid[(a,b)] != '#':
            g.add_edge((c,d), ((a,b), d), weight=1)
paths = list(nx.all_shortest_paths(g, (S, (1,0)), (E, (0,0)), "weight"))
for i in range(len(paths[0])-1):
    sol1 += g.edges[(paths[0][i], paths[0][i+1])]["weight"]
se = set()
for p in paths:
    for pl in p:
        se.add(pl[0])
sol2 = len(se)
print(sol1)
print(sol2)
