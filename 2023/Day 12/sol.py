from sys import stdin
from itertools import combinations

lines = [i.strip() for i in stdin.read().splitlines()]

def checkconf(springs, numbers):
    groups = [x for x in springs.split('.') if len(x)]
    if not len(groups) == len(numbers):
        return 0
    for i in range(len(numbers)):
        if not len(groups[i]) == numbers[i]:
            return 0
    return 1

solution = 0
solution2 = 0
for line in lines:
    springs, nums = line.split(' ')
    numbers = [int(i) for i in nums.split(',')]
    places_of_q = [i for i in range(len(springs)) if springs[i] == '?']
    needed_springs = sum(numbers)
    actual_springs = springs.count('#')
    perms = list(combinations(places_of_q, needed_springs-actual_springs))
    for p in perms:
        newspring = ''.join([springs[i] if i not in sorted(list(p)) else '#' for i in range(len(springs))])
        newspring = newspring.replace('?','.')
        solution += checkconf(newspring,numbers)
print("Part 1:",solution)
#7030194981795
