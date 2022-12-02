pointsE = {"A":1,"B":2,"C":3}
pointsP = {"X":1,"Y":2,"Z":3}

winpoints = {"AX":3,"AY":6,"AZ":0,"BX":0,"BY":3,"BZ":6,"CX":6,"CY":0,"CZ":3}

needed_choice = {"AX":"Z","AY":"X","AZ":"Y","BX":"X","BY":"Y","BZ":"Z","CX":"Y","CY":"Z","CZ":"X"}
part2_win = {"X":0,"Y":3,"Z":6}

import sys

score_part1 = 0
score_part2 = 0
for line in sys.stdin:
    x = line.split()
    score_part1 += winpoints["".join(x)] + pointsP[x[1]]
    score_part2 += part2_win[x[1]] + pointsP[needed_choice["".join(x)]]
    
print("Part 1:",score_part1)
print("Part 2:",score_part2)