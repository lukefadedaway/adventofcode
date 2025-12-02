def isinvalid(x, twice):
    if twice:
        return x == x[:(len(x)//2)]*2
    for i in range(1, len(x)//2 + 1):
        if len(x) % i == 0:
            if x == x[:i] * (len(x) // i):
                return True
    return False


ranges = input().strip().split(',')
sol1 = []
sol2 = []
for a,b in (r.split('-') for r in ranges):
    for i in range(int(a), int(b)+1, 1):
        if isinvalid(str(i), True):
            sol1.append(i)
        if isinvalid(str(i), False):
            sol2.append(i)
print(sum(sol1))
print(sum(sol2))