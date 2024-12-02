from sys import stdin 

def issave(l):
    if len(l) < 2:
        return 1
    if l[0] > l[1]:
        l.reverse()
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return 0
        if l[i] == l[i+1]:
            return 0
        if abs(l[i]-l[i+1]) > 3:
            return 0
    return 1

sol1 = 0
sol2 = 0
for line in stdin:
    lin = [int(x) for x in line.split()]
    save = issave(lin)
    sol1 += save
    sol2 += save
    save2 = 0
    if save == 0:
        for i in range(len(lin)):
            if issave(lin[:i] + lin[i+1:]) == 1:
                save2 = 1
    sol2 += save2
print(sol1)
print(sol2)