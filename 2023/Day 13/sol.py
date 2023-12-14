from sys import stdin

lines = [i.strip() for i in stdin.read().splitlines()]

def getnum(x):
    # Part 2: anstatt direkt s=-1, counter++, wenn counter>0 -> s=-1
    #print(x)
    sol = []
    s = -1
    for i in range(len(x)-1):
        if x[i] == x[i+1]:
            s = i
            break
    #print("s,",s,len(x)-s-1)
    if not s == -1:
        i = 0
        while (s-i) > -1 and ((len(x)-1) >= (s+i+1)):
            #print(((s//100)-1)-i,(s//100)+i)
            if not x[s-i] == x[s+i+1]:
                s = -1
                break
            i += 1
    if not s == -1:
        sol.append((s+1)*100)
    #print("s;",s)
    #if s == -1:
        #print("LR")
    s = -1
    for i in range(len(x[0])-1):
        eq = True
        for j in range(len(x)-1):
            if not x[j][i] == x[j][i+1]:
                eq = False
        if eq:
            s = i
            #print("s:",s)
            break
    if not s == -1 and s > 0:
        if (s+1) >= len(x[0]):
            for y in range(len(x)):
                x[y] = x[y][::-1]
            s = len(x[0]) - (s+1)
        i = 0
        #print(s, len(x[0]))
        while (s-i) > -1 and ((len(x[0])-1) >= (s+i+1)):
            for j in range(len(x)-1):
                #print(j,s-i,",",j,s+i+1)
                if not x[j][s-i] == x[j][s+i+1]:
                #if not x[s-i] == x[s+i+1]:
                    s = -1
                    break
            i += 1
    #print(s)
    if not s == -1:
        sol.append(s+1)
    #print("sol:",sol)
    return sum(sol)

def soll(s, d, n=0):
    sss = []
    g = { (x, y): s[y][x] for y in range(len(s)) for x in range(len(s[0])) }
    w = len(s[0])
    h = len(s)
    for m in range(1, w):
        if sum(g[(i,y)] != g.get((m-i+m-1,y), g[(i,y)]) for i in range(m) for y in range(h)) == d:
            n += m
            sss.append(m)
    for m in range(1, h):
        if sum(g[(x,i) ] != g.get((x,m-i+m-1), g[(x,i)]) for x in range(w) for i in range(m)) == d:
            n += 100 * m
            sss.append(100*m)
    #print("sss:",sss)
    return n

par = []
solution = []
sol = []
sol2 = []
for line in lines:
    if line:
        par.append(line)
    else:
        solution.append(getnum(par))
        sol.append(soll(par,0))
        sol2.append(soll(par,1))
        #if not sol[-1] == solution[-1]:
            #print(par)
            #print(solution[-1],sol[-1])
        par = []
solution.append(getnum(par))
sol.append(soll(par,0))
sol2.append(soll(par,1))
#print(par)
#print("Part 1:",sum(solution))
print("Part 1:", sum(sol))
print("Part 2:",sum(sol2))
