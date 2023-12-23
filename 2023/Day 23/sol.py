from sys import stdin
import sys
sys.setrecursionlimit(1000000)

lines = [i.strip() for i in stdin.read().splitlines()]
start = (0,1)
finish = (len(lines)-1, len(lines[0])-2)
p = "^>v<"
def addid(a,b):
    return (a[0]+b[0],a[1]+b[1])
def getvalidlist(a, l=[]):
    x = addid(a,(1,0))
    if x in graph:
        if lines[x[0]][x[1]] in "v.":
            l += [x]
    x = addid(a,(-1,0))
    if x in graph:
        if lines[x[0]][x[1]] in "^.":
            l += [x]
    x = addid(a,(0,1))
    if x in graph:
        if lines[x[0]][x[1]] in ">.":
            l += [x]
    x = addid(a,(0,-1))
    if x in graph:
        if lines[x[0]][x[1]] in "<.":
            l += [x]
    return l
    
graph = [(i,j) for i,line in enumerate(lines) for j,c in enumerate(line) if c != '#']

def search(node, dist=0, visited = set()):
    if node == finish: return dist
    if node in visited: return dist
    visited.add(node)
    lllll = getvalidlist(node, [])
    dist = max([search(a,dist+1,visited) for a in lllll if a in graph])
    visited.remove(node)
    return dist

print("Part 1:",search(start))
# 6670
