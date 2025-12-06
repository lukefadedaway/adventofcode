from sys import stdin 

numbers = []
numbers2 = []
numberlines = []

sol1 = 0
sol2 = 0
for line in stdin:
    if "+" not in line:
        numbers.append([int(x) for x in line.split()])
        numberlines.append(line[:-1][::-1])
    else:
        splitpoint = 0
        for i in range(len(numberlines[0])):
            x = set()
            for j in numberlines:
                x.add(j[i])
            if len(list(x)) == 1 and ' ' in list(x):
                nn = []
                for j in numberlines:
                    nn.append(j[splitpoint:i])
                splitpoint = i+1
                part = []
                for j in range(len(nn[0])):
                    part.append(int(''.join(k[j] for k in nn)))
                numbers2.append(part)
        nn = []
        for j in numberlines:
            nn.append(j[splitpoint:])
        part = []
        for j in range(len(nn[0])):
            part.append(int(''.join(k[j] for k in nn)))
        numbers2.append(part)
        numbers2 = numbers2[::-1]
        p = line.strip().split()
        for i in range(len(p)):
            parsol = 0
            parsol2 = 0
            if p[i] == '*':
                parsol = 1
                parsol2 = 1
                for j in numbers:
                    parsol *= j[i] 
                for j in numbers2[i]:
                    parsol2 *= j
            if p[i] == '+':
                for j in numbers:
                    parsol += j[i]
                parsol2 = sum(numbers2[i])
            sol1 += parsol
            sol2 += parsol2
print(sol1)
print(sol2)