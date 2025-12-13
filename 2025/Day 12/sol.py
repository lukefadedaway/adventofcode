from sys import stdin

lines = [line.rstrip("\n") for line in stdin if line.strip() != ""]

shapes = {}
regions = []

i = 0
n = len(lines)
sol1 = 0

while i < n and "x" not in lines[i]:
    idx_str = lines[i].split(":")[0]
    shape_idx = int(idx_str)
    i += 1
    c = 0
    shape = []
    while i < n and all(c in "#." for c in lines[i]):
        shape.append(lines[i])
        i += 1
        c += lines[i].count('#')
    shapes[shape_idx] = {"shape":shape, "counts":c}

while i < n:
    header, *counts = lines[i].split()
    dims = header.split(":")[0]
    w, h = map(int, dims.split("x"))
    counts = list(map(int, counts))

    regions.append({
        "width": w,
        "height": h,
        "counts": counts
    })
    i += 1
    blocks = 0
    for j in range(len(counts)):
        blocks += shapes[j]["counts"]
    if blocks <= w*h and sum(counts)*9 <= w*h:
        sol1 += 1
print(sol1)
