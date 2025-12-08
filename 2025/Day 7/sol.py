from sys import stdin 

grid = [line.strip() for line in stdin]
cur = [0] * len(grid[0])
sol1 = 0

for g in grid:
    nex = [i for i in cur]
    for i in range(len(g)):
        if g[i] == 'S':
            nex[i] = 1
        if g[i] == '^':
            if cur[i] > 0:
                sol1 += 1
                nex[i-1] += cur[i]
                nex[i+1] += cur[i]
                nex[i] = 0
    cur = [i for i in nex]
print(sol1)
print(sum(cur))