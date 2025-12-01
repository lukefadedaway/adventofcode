from sys import stdin 

val = 50
sol1 = 0
sol2 = 0
for line in stdin:
    v = int(line[1:])
    if line[0] == 'L':
        v *= -1
    oval = val
    val = (val + v) 
    if val < 0:
        sol2 += abs((100+val)//100)
        if oval != 0:
            sol2 += 1
    if v > 0:
        sol2 += val // 100
    val = val % 100
    if val == 0:
        sol1 += 1
    if v < 0 and val == 0:
        sol2 += 1
print(sol1)
print(sol2)