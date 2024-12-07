from sys import stdin
import re

def test(L, pres, goal):
    if pres > goal:
        return False
    if L == []:
        return pres == goal
    if pres == goal:
        if L == []:
            return True
        else:
            for i in L:
                if i > 1:
                    return False
    return max(test(L[1:], pres+L[0], goal), test(L[1:], pres*L[0], goal))

def test2(L, pres, goal):
    if pres > goal:
        return False
    if L == []:
        return pres == goal
    if pres == goal:
        if L == []:
            return True
        else:
            for i in L:
                if i > 1:
                    return False
    newpres = int(str(pres) + str(L[0]))
    return max(test2(L[1:], pres+L[0], goal), test2(L[1:], pres*L[0], goal), test2(L[1:], newpres, goal))

sol1 = 0
sol2 = 0
for line in stdin:
    g, n = line.split(":")
    goal = int(g)
    nums = [int(x) for x in n.split()]
    if test(nums, 0, goal):
        sol1 += goal
    if test2(nums, 0, goal):
        sol2 += goal
print(sol1)
print(sol2)