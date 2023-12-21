from sys import stdin
from queue import Queue
import numpy as np

lines = ["#"+i.strip()+"#" for i in stdin.read().splitlines()]
lines = ['#' * len(lines[1])] + lines + ['#' * len(lines[1])]

def runit(lin, n, sol = 0):
    visited = [[set() for c in line] for line in lin]
    spos = [0,0]
    if n > 64:
        spos = [len(lin) // 2, len(lin[0]) // 2]
    else:
        for i in range(len(lines)):
            for j in range(len(lines[0])):
                if lin[i][j] == 'S':
                    spos = [i,j]
    q = Queue()
    q.put((spos[0],spos[1],1))
    run = True
    while run and q.qsize():
        x,y,p = q.get()
        if p < n+1:
            for m in [[0,1],[0,-1],[1,0],[-1,0]]:
                x1 = x+m[0]
                y1 = y+m[1]
                if not lin[x1][y1] == '#' and len(visited[x1][y1]) == 0:
                    visited[x1][y1].add(p)
                    q.put((x1,y1,p+1))
        if p > n:
            run = False
    for v in visited:
        for vv in v:
            ad = 0
            ad1 = 0
            for vvv in vv:
                if vvv % 2 == 0 and vvv < n+1:
                        ad = 1
                else:
                    if vvv % 2 == 1 and vvv < n+1:
                        ad1 += 1
            if n % 2 == 0:
                sol += ad
            else:
                sol += ad1
    return sol

part2lines = []
for i in range(5):
    for j in range(1,len(lines)-1):
            part2lines += [lines[j][1:-1].replace('S','.') * 5]
a0 = runit(part2lines, 65)
a1 = runit(part2lines, 65 + 131)
a2 = runit(part2lines, 65 + 2 * 131)
vandermonde = np.matrix([[0, 0, 1], [1, 1, 1], [4, 2, 1]])
b = np.array([a0, a1, a2])
x = np.linalg.solve(vandermonde, b).astype(np.int64)
# Polynom für die Anzahl der Felder, da wiederholender Ablauf (alle 2 * 131 Schritte -> quadratisches Polynom für Anzahl)
# 2 * 131 da ungerade Anzahl an Schritten gegeben
# Berechnung aus f(n0), f(n1), f(n2) -> f(nn) mit nn = 26501365
# 26501365 = 202300 * 131 + 65 , 131 = len(lines[0])
n = 202300

solution = runit(lines,64)
solution2 = x[0] * n * n + x[1] * n + x[2]
print("Part 1:", solution)
print("Part 2:",solution2)
