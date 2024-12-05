from sys import stdin
import re

def checkrules(line, rules):
    t = [int(a) for a in line.strip().split(",")]
    for i in range(len(t)):
        x = t[i]
        for j in range(i):
            if x not in rules:
                continue
            if t[j] in rules[x]:
                return 0
    return t[len(t)//2]

# too high on real input, 5434 > 5184
# does not produce correct lines by only swapping the mistakes 
def checkrules2(line, rules):
    t = [int(a) for a in line.strip().split(",")]
    i = 0
    while i < len(t):
        x = t[i]
        for j in range(i):
            if x not in rules:
                continue
            if t[j] in rules[x]:
                temp = t[j]
                t[j] = x
                t[i] = temp
                i = -1
        i += 1
    print("c2",checkrules(line, rules))
    return t[len(t)//2]

rules_banned_predecessors = {}
rulesection = True
sol1 = 0
sol2 = 0
for line in stdin:
    if len(line) < 2:
        rulesection = False
        continue
    if rulesection:
        a,b = line.strip().split("|")
        if int(a) in rules_banned_predecessors:
            rules_banned_predecessors[int(a)].append(int(b))
        else:
            rules_banned_predecessors[int(a)] = [int(b)]
    else:
        s = checkrules(line, rules_banned_predecessors)
        sol1 += s
        if s == 0:
            sol2 += checkrules2(line, rules_banned_predecessors)
print(sol1)
print(sol2)