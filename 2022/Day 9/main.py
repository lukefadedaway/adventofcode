import sys
import math
head = [0,0]
tail = [0,0]
rope2 = [[0,0] for _ in range(10)]
visited = set()
visited.add((tail[0],tail[1]))
visited2 = set()
visited2.add((tail[0],tail[1]))
iterations = 0

def distance(h,t):
    return math.dist(h, t)

getsteps = {"R": (1,0),"U": (0,1),"L": (-1,0),"D": (0,-1)}
def updateTail(h,t):
    if h[0] == t[0]:
        if h[1] > t[1]+1:
            t[1] += 1
        if h[1] < t[1]-1:
            t[1] -= 1
    elif h[1] == t[1]:
        if h[0] > t[0]+1:
            t[0] += 1
        if h[0] < t[0]-1:
            t[0] -= 1
    elif distance(h,t) > 1.5:
        if h[0] > t[0]:
            t[0] += 1
        elif h[0] < t[0]:
            t[0] -= 1
        if h[1] > t[1]:
            t[1] += 1
        elif h[1] < t[1]:
            t[1] -= 1

for line in sys.stdin:
    direction, amount = line.split()
    step = getsteps[direction]
    for x in range(int(amount)):
        iterations = min(iterations+1, 9)
        head[0] += step[0]
        head[1] += step[1]
        rope2[0] = head
        updateTail(head,tail)
        visited.add((tail[0],tail[1]))
        for y in range(0,iterations):
            updateTail(rope2[y],rope2[y+1])
        visited2.add((rope2[9][0],rope2[9][1]))
print("Part 1:")
print(len(visited))
print("Part 2:")
print(len(visited2))