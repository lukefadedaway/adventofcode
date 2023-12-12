from sys import stdin
from itertools import combinations
from  functools import cache

lines = [i.strip() for i in stdin.read().splitlines()]
orignums = (0,) * 100

@cache
def checkconf(springs, numbers, curr):
    if not springs:
        return (numbers or (0,)) == (curr,)
        
    s = 0
    if springs[0] == '?':
        s += checkconf('.'+springs[1:],numbers, curr)
        s += checkconf('#'+springs[1:],numbers, curr)
        
    if springs[0] == '#' and numbers and curr < numbers[0]:
        s += checkconf(springs[1:],numbers, curr+1)
    
    if springs[0] == '.':
        if numbers and curr == numbers[0]:
            s += checkconf(springs[1:],numbers[1:], 0)
        if not numbers or curr == 0:
            s += checkconf(springs[1:],numbers, 0)
    return s
    
@cache
def checkconf2(springs, numbers):
    if (numbers or (0,)) == (0,) and springs.count('#') > 0:
        return 0
    if not springs:
        return (numbers or (0,)) == (0,)
    s = 0
    
    if springs[0] == '?':
        s += checkconf2('#'+springs[1:],numbers)
        s += checkconf2('.'+springs[1:],numbers)
    if springs[0] == '.':
        if numbers and 0 == numbers[0]:
            s += checkconf2(springs[1:],numbers[1:])
        if not numbers or numbers[0] == orignums[-len(numbers)]:
            s += checkconf2(springs[1:],numbers)
    if springs[0] == '#' and numbers and numbers[0] > 0:
        s += checkconf2(springs[1:],(numbers[0]-1,)+ numbers[1:])
    return s
    
solution = 0
solution2 = 0
for line in lines:
    springs, nums = line.split(' ')
    numbers = tuple([int(i) for i in nums.split(',')])
    orignums = numbers
    solution += checkconf(springs, numbers, 0)
    orignums = numbers * 5
    solution2 += checkconf('?'.join([springs]  * 5), numbers * 5, 0)
print("Part 1:",solution)
print("Part 2:",solution2, solution2 == 7030194981795)
