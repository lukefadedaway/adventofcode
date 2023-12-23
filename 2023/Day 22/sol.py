from sys import stdin

lines = [i.strip() for i in stdin.read().splitlines()]
boxes = []
for line in lines:
    boxa, boxb = [l.split(',') for l in line.split('~')]
    boxes.append((int(boxa[0]),int(boxa[1]),int(boxa[2]),int(boxb[0]),int(boxb[1]),int(boxb[2])))
boxes = sorted(boxes, key=lambda x: min(x[2],x[5]))

def boxoverlap(a,b):
    xA = max(a[0], b[0])
    yA = max(a[1], b[1])
    xB = min(a[3], b[3])+1
    yB = min(a[4], b[4])+1

    interArea = abs(max((xB - xA, 0)) * max((yB - yA), 0))
    if interArea == 0:
        return False
    return True
    
for i in range(len(boxes)):
    if boxes[i][2] == 1 or (boxes[i-1][2] == boxes[i][2]-1 and boxoverlap(boxes[i-1],boxes[i])):
        continue
    sitontop = [x for x in boxes[:i] if boxoverlap(x,boxes[i])]
    if len(sitontop) == 0:
        m = min(boxes[i][2],boxes[i][5])-1
        boxes[i] = (boxes[i][0],boxes[i][1],boxes[i][2]-m,boxes[i][3],boxes[i][4],boxes[i][5]-m)
        continue
    dropdist = min(boxes[i][2],boxes[i][5]) - max(sitontop[-1][2],sitontop[-1][5]) - 1
    boxes[i] = (boxes[i][0],boxes[i][1],boxes[i][2]-dropdist,boxes[i][3],boxes[i][4],boxes[i][5]-dropdist)

boxesabove = [[] for _ in range(len(boxes))]
for i in range(len(boxes)):
    boxesabove[i] = [n for n,x in enumerate(boxes) if boxoverlap(x,boxes[i]) and min(x[2],x[5]) == min(boxes[i][2],boxes[i][5])+1]
boxesbelow = [[] for _ in range(len(boxes))]
for i in range(len(boxes)):
    boxesbelow[i] = [n for n,x in enumerate(boxes) if boxoverlap(x,boxes[i]) and min(x[2],x[5])+1 == min(boxes[i][2],boxes[i][5])]
solution = [0 for _ in range(len(boxes))]
#print(boxesabove)
#print(boxesbelow)
#print(max([(boxoverlap(boxes[i],boxes[i+1]) and max(boxes[i][2],boxes[i][5]) == max(boxes[i+1][2],boxes[i+1][5])) for i in range(len(boxes)-1)]))
for i in range(len(boxes)):
    if len(boxesabove[i]) == 0:
        solution[i] = 1
        continue
    if i > 0:
        if len([x for x in boxesabove[i] if len(boxesbelow[x]) > 1]) == len(boxesabove[i]):
            solution[i] = 1
print("Part 1:",sum(solution)) # 441
# 80778
