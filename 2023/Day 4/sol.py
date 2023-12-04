from sys import stdin
import re

solution = []
lines = stdin.read().splitlines()
solution2 = [1 for _ in lines]
index = -1
for line in lines:
    index += 1
    game, card = line.strip().split(':')
    winner, miner = card.strip().split('|')
    win = sorted([i for i in winner.split(' ') if len(i) > 0])
    mine = sorted([i for i in miner.split(' ') if len(i) > 0])
    incommon = len(set(win).intersection(set(mine)))
    if incommon > 0:
        solution.append(2**(incommon-1))
        for x in range(incommon):
            solution2[index + x + 1] += solution2[index]
        continue
print("Part 1:",sum(solution))
print("Part 2:",sum(solution2))
