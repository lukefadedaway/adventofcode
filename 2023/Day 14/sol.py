from sys import stdin

lines = [i.strip() for i in stdin.read().splitlines()]
cache = {}

def rotateanddrop(a, rev = True):
    s = [''.join(row) for row in zip(*[reversed(row) for row in a])]
    s = [''.join(row) for row in zip(*[reversed(row) for row in s])]
    s = [''.join(row) for row in zip(*[reversed(row) for row in s])]
    for i in range(len(s)):
        par = s[i].split('#')
        pars=[]
        for p in par:
            pars += [p,'#' if len(p)>0 else '#']
        news = ''.join(''.join(sorted(p)) for p in pars)
        s[i] = news[:-1]
    return s
    
def getscore(a, current_cycles, sol=0):
    s = [x for x in a]
    for i in range((current_cycles+2)%4):
        s = [''.join(row) for row in zip(*[reversed(row) for row in s])]
    for i in range(len(s)):
        sol += (i+1)*s[i].count('O')
    return sol

def putindict(a, current_cycles):
    if tuple(a) in cache:
        return cache[tuple(a)]
    cache[tuple(a)] = current_cycles
    return -1

def part2(a):
    cycles = 1000000000
    current_cycles = 1
    for i in range(3):
        a = rotateanddrop(a,(i%2 == 1))
    while current_cycles < cycles:
        check = putindict(a,current_cycles)
        if check == -1:
            current_cycles += 1
            for i in range(4):
                a = rotateanddrop(a,(i%2 == 0))
            continue
        
        length = current_cycles - check
        current_cycles = cycles - ((cycles - current_cycles) % length)
        while current_cycles < cycles:
            current_cycles += 1
            for i in range(4):
                a = rotateanddrop(a,(i%2 == 0))
    return getscore(a,cycles)
    
putindict(lines,0)
lines = rotateanddrop(lines)

print("Part 1:",getscore(lines,1))
print("Part 2:",part2(lines))
