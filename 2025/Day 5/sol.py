from sys import stdin 

def merge_intervals(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda v: v[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])
    return merged

ranges = []
sol1 = 0
isrange = True
for line in stdin:
    if len(line.strip()) < 1:
        isrange = False
        continue
    if isrange:
        ranges.append([int(x) for x in line.split('-')])
    else:
        x = int(line)
        if any(n[0] <= x <= n[1] for n in ranges):
            sol1 += 1
print(sol1)
print(sum([b-a+1 for a,b in merge_intervals(ranges)]))