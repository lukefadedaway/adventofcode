from sys import stdin

lines = [i.strip() for i in stdin.read().splitlines()]
dirs = {"R": (0,1), "L": (0,-1), "U": (-1,0), "D": (1,0)}
dirs2 = {0:"R", 1:"D", 2:"L", 3:"U"}

def calculate_polygon_area(coordinates):
    n = len(coordinates)
    if n < 3:
        raise ValueError("A polygon must have at least 3 vertices.")
    area = 0.5 * sum((coordinates[i][0] * coordinates[(i + 1) % n][1] -
                     coordinates[(i + 1) % n][0] * coordinates[i][1])
                    for i in range(n))
    return abs(area)

coordinates = [(0,0)]
coordinates2 = [(0,0)]
border = set()
border2 = set()
for line in lines:
    dir, leng, col = line.split(" ")
    dir2 = dirs2[int(col[-2])]
    leng2 = int(col[2:-2],16)
    curX, curY = coordinates[-1]
    curX2, curY2 = coordinates2[-1]
    for i in range(int(leng)+1):
        border.add((curX + i*dirs[dir][0], curY + i*dirs[dir][1]))
    for i in range(int(leng2)+1):
        border2.add((curX2 + i*dirs[dir2][0], curY2 + i*dirs[dir2][1]))
    coordinates.append((coordinates[-1][0] + (int(leng)*dirs[dir][0]), coordinates[-1][1] + (int(leng)*dirs[dir][1])))
    coordinates2.append((coordinates2[-1][0] + (int(leng2)*dirs[dir2][0]), coordinates2[-1][1] + (int(leng2)*dirs[dir2][1])))
    
solution = (calculate_polygon_area(coordinates) + 1 - len(border) // 2) + len(border)
solution2 = (calculate_polygon_area(coordinates2) + 1 - len(border2) // 2) + len(border2)
print("Part 1:", int(solution))
print("Part 2:", int(solution2))
