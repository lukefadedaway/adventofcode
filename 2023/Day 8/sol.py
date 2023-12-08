from sys import stdin
from math import gcd
def kgv(a, b):
    return a * b // gcd(a, b)
    
def kgv_list(nums):
    result = nums[0]
    for num in nums[1:]:
        result = kgv(result, num)
    return result

lines = [i.strip() for i in stdin.read().splitlines()]
path = lines[0].replace('L','0').replace('R','1')
current = "AAA"
graph = {}

for line in lines[-(len(lines)-2):]:
    partl = line.split(" = ")
    graph[partl[0]] = [''.join(char for char in partl[1].split(',')[0] if char.isalpha()),''.join(char for char in partl[1].split(',')[1] if char.isalpha())]
current2 = [a for a in graph.keys() if a[2] == 'A']
counter = 0
counter2 = 0
counter2s = []
pathpos = 0
while not current == "ZZZ":
    counter += 1
    current = graph[current][int(path[pathpos])]
    pathpos += 1
    pathpos %= len(path)
pathpos = 0
while len(current2) > 0 and not set([x[2] for x in current2]) == set(['Z']):
    counter2 += 1
    to_drop = []
    for i in range(len(current2)):
        current2[i] = graph[current2[i]][int(path[pathpos])]
        if current2[i][2] == 'Z':
            to_drop.append(current2[i])
            counter2s.append(counter2)
    current2 = [x for x in current2 if x not in to_drop]
    pathpos += 1
    pathpos %= len(path)
print("Part 1:",counter)
print("Part 2:",kgv_list(counter2s))
