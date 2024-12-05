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

def checkrules2(line, rules):
    t = [int(a) for a in line.strip().split(",")]
    tn = []
    for x in t:
        if tn == []:
            tn.append(x)
        else:
            index = len(tn)
            for i in range(len(tn)-1, -1, -1):
                a = tn[i]
                if a not in rules:
                    index -= 1
                    continue
                if x not in rules[a]:
                    index -= 1
                    continue
                if x in rules[a]:
                    break
            tn = tn[:index] + [x] + tn[index:]
    return tn[len(t)//2]

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