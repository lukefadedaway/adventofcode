from sys import stdin

lines = [i.strip() for i in stdin.read().split(',')]
boxes = [[] for _ in range(256)]

def step(par,s = 0):
    for c in par:
        s += ord(c)
        s *= 17
        s %= 256
    return s
    
def find_index(lst, substring_a):
    for index, item in enumerate(lst):
        if item.startswith(substring_a):
            return index
    return -1

solution = [step(x) for x in lines]
solution2 = []
for i in range(len(lines)):
    if lines[i][-1] == '-':
        hash = step(lines[i][:-1])
        boxes[hash] = [x for x in boxes[hash] if not x.startswith(lines[i][:-1])]
        continue
    hash = step(lines[i].split('=')[0])
    check = find_index(boxes[hash],lines[i].split('=')[0])
    if check == -1:
        boxes[hash] += [lines[i]]
    boxes[hash] = [lines[i] if x.startswith(lines[i].split('=')[0]) else x for x in boxes[hash]]
for i in range(len(boxes)):
    for j in range(len(boxes[i])):
        s = (i+1)
        s *= (j+1)
        s *= int(boxes[i][j].split('=')[1])
        solution2.append(s)
print("Part 1:",sum(solution))
print("Part 2:",sum(solution2))
