from sys import stdin

def process_tuples(tuples_list, x):
    possible = []
    for t in tuples_list:
        if t[0] <= x and x < t[0] + t[2]:
            possible.append(x - t[0] + t[1])
    if len(possible) < 1:
        return x
    return min(possible)

solution = []
lines = [line for line in stdin.read().splitlines() if len(line) > 0]
seeds = [int(s) for s in lines[0].split(':')[1].strip().split(' ')]

translation = []
for i in range(len(lines)):
    if not lines[i][0].isnumeric():
        #translation.sort(key=lambda x: x[0])
        if len(translation) > 0:
            for j in range(len(seeds)):
                seeds[j] = process_tuples(translation, seeds[j])
        translation = []
        continue
    line = lines[i].split(' ')
    translation.append((int(line[1]), int(line[0]), int(line[2])))
if len(translation) > 0:
    for j in range(len(seeds)):
        seeds[j] = process_tuples(translation, seeds[j])
print("Part 1:",min(seeds))
# Part 2: 31161857
