from sys import stdin 

grid = ['.' + line.strip() + '.' for line in stdin]
grid = ['.'*len(grid[1])] + grid + ['.'*len(grid[1])]
rem = []

sol = 0
for i in range(1,len(grid)):
    for j in range(1,len(grid[1])):
        if grid[i][j] == '@':
            if [grid[i-1][j-1],grid[i-1][j],grid[i-1][j+1],grid[i][j-1],grid[i][j+1],grid[i+1][j-1],grid[i+1][j],grid[i+1][j+1]].count('@') < 4:
                sol += 1
                rem.append((i,j))
print(sol)
while len(rem) > 0:
    for a,b in rem:
        grid[a] = grid[a][:b] + '.' + grid[a][(b+1):]
    rem = []
    for i in range(1,len(grid)):
        for j in range(1,len(grid[1])):
            if grid[i][j] == '@':
                if [grid[i-1][j-1],grid[i-1][j],grid[i-1][j+1],grid[i][j-1],grid[i][j+1],grid[i+1][j-1],grid[i+1][j],grid[i+1][j+1]].count('@') < 4:
                    sol += 1
                    rem.append((i,j))
print(sol)