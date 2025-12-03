from sys import stdin 

sol1 = []
sol2 = []
for l in stdin:
    line = l.strip()
    max1, max2 = 0, 0
    maxpos = 0 
    for i in range(len(line)-1):
        if int(line[i]) > max1:
            max1 = int(line[i])
            maxpos = i+1
    for i in range(maxpos, len(line)):
        if int(line[i]) > max2:
            max2 = int(line[i])
    sol1.append(max1*10 + max2)
    max1 = 0
    nsol = []
    maxpos = 0
    for i in range(len(line)-11):
        if int(line[i]) > max1:
            max1 = int(line[i])
            maxpos = i+1
    nsol.append(str(max1))
    for j in range(10,-1,-1):
        max1 = 0
        for i in range(maxpos,len(line)-j):
            if int(line[i]) > max1:
                max1 = int(line[i])
                maxpos = i+1
        nsol.append(str(max1))
    sol2.append(int(''.join(nsol)))
print(sum(sol1))
print(sum(sol2))
    