from sys import stdin
from itertools import combinations

lines = [i.strip() for i in stdin.read().splitlines()]

def line_intersect(lanes, sol=0):
    mini, maxi = 200_000_000_000_000, 400_000_000_000_000
    for l1, l2 in combinations(lanes, 2):
        x1, y1, _, xm1, ym1, _ = l1
        xp2, y2, _, xm2, ym2, _ = l2

        if ym1*xm2 == ym2*xm1:
            continue
        t1 = (ym2*(x1-xp2) - xm2*(y1-y2))/(ym1*xm2 - xm1*ym2)
        t2 = (ym1*(xp2-x1) - xm1*(y2-y1))/(ym2*xm1 - xm2*ym1)
        if t1 < 0 or t2 < 0:
            continue
        x = x1 + t1*xm1
        y = y1 + t1*ym1

        if mini <= x <= maxi and mini <= y <= maxi:
            sol += 1
    return sol

lanes = []
for i in range(len(lines)):
    a,b = lines[i].split('@')
    c = [int(x) for x in a.strip().split(',')]
    d = [int(x) for x in b.strip().split(',')]
    lanes += [(c[0],c[1],c[2],d[0],d[1],d[2])]

print("Part 1:",line_intersect(lanes))
# 527310134398221
