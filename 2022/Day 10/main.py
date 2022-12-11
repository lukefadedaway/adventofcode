import sys
import math

signalstrengths = []
curtime = 1
curX = 1
part2 = ""
part2dict = {True:"#",False:"."}

def vicinity(time, x):
    return abs(time - x) <= 1

for line in sys.stdin:
    if line == "noop\n":
        if (curtime+20) % 40 == 0 and curtime > 0:
            signalstrengths.append(curX * curtime)
        part2 += part2dict[vicinity((curtime-1)%40,curX)]
        curtime += 1
    elif line[0] == "a":
        a, ad = line.split()
        if (curtime+20) % 40 == 0 and curtime > 0:
            signalstrengths.append(curX * curtime)
        part2 += part2dict[vicinity((curtime-1)%40,curX)]
        curtime += 1
        if (curtime+20) % 40 == 0 and curtime > 0:
            signalstrengths.append(curX * curtime)
        part2 += part2dict[vicinity((curtime-1)%40,curX)]
        curtime += 1
        curX += int(ad)
        
print("Part 1:")
print(sum(signalstrengths))
print("Part 2:")
print(part2[0:39])
print(part2[40:79])
print(part2[80:119])
print(part2[120:159])
print(part2[160:199])
print(part2[200:])