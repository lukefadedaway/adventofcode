from sys import stdin

lines = [i.strip() for i in stdin.read().splitlines()]
grid = [[[] for _ in range(len(lines[0]))] for _ in range(len(lines))]

updatemove = {"-": {(0,1):[(0,1)], (0,-1):[(0,-1)], (1,0): [(0,1),(0,-1)], (-1,0): [(0,1),(0,-1)]}, "|": {(1,0):[(1,0)], (-1,0):[(-1,0)], (0,1): [(1,0),(-1,0)], (0,-1): [(1,0),(-1,0)]}, "/": {(0,1):[(-1,0)], (0,-1):[(1,0)], (1,0): [(0,-1)], (-1,0): [(0,1)]}, "\\": {(0,1):[(1,0)], (0,-1):[(-1,0)], (1,0): [(0,1)], (-1,0): [(0,-1)]}}

class Beam:
    beams_list = []
    
    def __init__(self, position=[0, 0], orientation=(0, 1)):
        self.position = position
        self.orientation = orientation
        Beam.beams_list.append(self)
        
    def move(self):
        if self.position[0] >= len(lines) or self.position[1] >= len(lines[0]) or self.position[0] < 0 or self.position[1] < 0:
            Beam.beams_list.remove(self)
            return
        tile = lines[self.position[0]][self.position[1]]
        if self.orientation in grid[self.position[0]][self.position[1]]:
             Beam.beams_list.remove(self)
             return
        grid[self.position[0]][self.position[1]].append(self.orientation)
        if not tile == '.':
            nextmoves = updatemove[tile][self.orientation]
            if len(nextmoves) > 1:
                newbeam = Beam(position=[self.position[0] + nextmoves[1][0], self.position[1] + nextmoves[1][1]], orientation=nextmoves[1])
            self.position[0] += nextmoves[0][0]
            self.position[1] += nextmoves[0][1]
            self.orientation = nextmoves[0]
            return
        self.position[0] += self.orientation[0]
        self.position[1] += self.orientation[1]

thebeam = Beam()
while len(Beam.beams_list) > 0:
    for b in Beam.beams_list:
        b.move()
solution = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if len(grid[i][j]) > 0:
            solution += 1
part2list = [(x,0,0,1) for x in range(len(lines))]
part2list += [(x,len(lines[0])-1,0,-1) for x in range(len(lines))]
part2list += [(0,y,1,0) for y in range(len(lines[0]))]
part2list += [(len(lines)-1,y,-1,0) for y in range(len(lines[0]))]
solution2 = 0
for a in part2list:
    grid = [[[] for _ in range(len(lines[0]))] for _ in range(len(lines))]
    thebeam = Beam(position=[a[0],a[1]], orientation=(a[2],a[3]))
    while len(Beam.beams_list) > 0:
        for b in Beam.beams_list:
            b.move()
    sol = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if len(grid[i][j]) > 0:
                sol += 1
    solution2 = max(sol,solution2)
print("Part 1:", solution)
print("Part 2:", solution2)
