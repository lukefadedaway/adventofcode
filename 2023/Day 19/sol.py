from sys import stdin

lines = [i.strip() for i in stdin.read().splitlines()]
split_index = lines.index("")
rules = lines[:split_index]
objects = lines[split_index+1:]

rulz = {}
for rule in rules:
    name, r = rule.split("{")
    rulz[name] = r[:-1].split(",")
solution = 0

for obj in objects:
    cont = True
    tobj = obj.strip('{}').split(',')
    x = int(tobj[0].split('=')[1])
    m = int(tobj[1].split('=')[1])
    a = int(tobj[2].split('=')[1])
    s = int(tobj[3].split('=')[1])
    curR = rulz["in"]
    while cont:
        for r in curR:
            rr = r.split(':')
            if len(rr) == 1:
                if r == "A":
                    solution += (x+m+a+s)
                    cont = False
                    break
                if r == "R":
                    cont = False
                    break
                curR = rulz[r]
                break
            if eval(rr[0]):
                newr = rr[1]
                if newr == "A":
                    solution += (x+m+a+s)
                    cont = False
                    break
                if newr == "R":
                    cont = False
                    break
                curR = rulz[newr]
                break
print("Part 1:",solution)
# 122756210763577

"""
valids = set()
def part2(curR,x,m,a,s,sol=0):
    for r in curR:
        newx = [100000000,-100000000]
        newm = [100000000,-100000000]
        newa = [100000000,-100000000]
        news = [100000000,-100000000]
        if r == "A":
            sol += (x[1]-x[0])*(m[1]-m[0])*(a[1]-a[0])*(s[1]-s[0])
            continue
        if r == "R":
            continue
        rr = r.split(':')
        if rr[0].count('<') > 0:
            rrr = rr[0].split('<')
            match rrr[0]:
                case "x":
                    newx = [x[0],min(x[1],int(rrr[1]))]
                    if newx[0] <= newx[1]:
                        if rr[1] == "A":
                            sol += (x[1]-x[0])*(m[1]-m[0])*(a[1]-a[0])*(s[1]-s[0])
                        elif rr[1] == "R":
                            sol += 0
                        else:
                            sol += part2(rulz[rr[1]], newx,m,a,s)
                case "m":
                    newm = [m[0],min(m[1],int(rrr[1]))]
                    if newm[0] <= newm[1]:
                        if rr[1] == "A":
                            sol += (x[1]-x[0])*(m[1]-m[0])*(a[1]-a[0])*(s[1]-s[0])
                        elif rr[1] == "R":
                            sol += 0
                        else:
                            sol += part2(rulz[rr[1]], x,newm,a,s)
                case "a":
                    newa = [a[0],min(a[1],int(rrr[1]))]
                    if newa[0] <= newa[1]:
                        if rr[1] == "A":
                            sol += (x[1]-x[0])*(m[1]-m[0])*(a[1]-a[0])*(s[1]-s[0])
                        elif rr[1] == "R":
                            sol += 0
                        else:
                            sol += part2(rulz[rr[1]], x,m,newa,s)
                case "s":
                    news = [s[0],min(s[1],int(rrr[1]))]
                    if news[0] <= news[1]:
                        if rr[1] == "A":
                            sol += (x[1]-x[0])*(m[1]-m[0])*(a[1]-a[0])*(s[1]-s[0])
                        elif rr[1] == "R":
                            sol += 0
                        else:
                            sol += part2(rulz[rr[1]], x,m,a,news)
        if rr[0].count('>') > 0:
            rrr = rr[0].split('>')
            match rrr[0]:
                case "x":
                    newx = [max(x[0],int(rrr[1])),x[1]]
                    if newx[0] <= newx[1]:
                        if rr[1] == "A":
                            sol += (x[1]-x[0])*(m[1]-m[0])*(a[1]-a[0])*(s[1]-s[0])
                        elif rr[1] == "R":
                            sol += 0
                        else:
                            sol += part2(rulz[rr[1]], newx,m,a,s)
                case "m":
                    newm = [max(m[0],int(rrr[1])),m[1]]
                    if newm[0] <= newm[1]:
                        if rr[1] == "A":
                            sol += (x[1]-x[0])*(m[1]-m[0])*(a[1]-a[0])*(s[1]-s[0])
                        elif rr[1] == "R":
                            sol += 0
                        else:
                            sol += part2(rulz[rr[1]], x,newm,a,s)
                case "a":
                    newa = [max(a[0],int(rrr[1])),a[1]]
                    if newa[0] <= newa[1]:
                        if rr[1] == "A":
                            sol += (x[1]-x[0])*(m[1]-m[0])*(a[1]-a[0])*(s[1]-s[0])
                        elif rr[1] == "R":
                            sol += 0
                        else:
                            sol += part2(rulz[rr[1]], x,m,newa,s)
                case "s":
                    news = [max(s[0],int(rrr[1])),s[1]]
                    if news[0] <= news[1]:
                        if rr[1] == "A":
                            sol += (x[1]-x[0])*(m[1]-m[0])*(a[1]-a[0])*(s[1]-s[0])
                        elif rr[1] == "R":
                            sol += 0
                        else:
                            sol += part2(rulz[rr[1]], x,m,a,news)
        if len(rr) == 1:
            newx2 = [min(x[0],newx[0]),max(x[1],newx[1])]
            newm2 = [min(m[0],newm[0]),max(m[1],newm[1])]
            newa2 = [min(a[0],newa[0]),max(a[1],newa[1])]
            news2 = [min(s[0],news[0]),max(s[1],news[1])]
            sol += part2(rulz[rr[0]], newx2,newm2,newa2,news2)
    valids.add((tuple(x),tuple(m),tuple(a),tuple(s)))
    return sol
solution2 = part2(rulz['in'],[0,4000],[0,4000],[0,4000],[0,4000])
solution3 = 0
for t in valids:
    x,m,a,s = t
    solution3 += (x[1]-x[0]+1)*(m[1]-m[0]+1)*(a[1]-a[0]+1)*(s[1]-s[0]+1)
"""
