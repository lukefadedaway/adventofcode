from sys import stdin
from functools import cmp_to_key

compare_chars = {'2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'J': 10, 'Q': 11, 'K': 12, 'A': 13}
part2 = False

def compare_cards(ca,cb):
    a = ca[0]
    b = cb[0]
    scorea = 1
    scoreb = 1
    seta = list(set(a))
    setb = list(set(b))
    if len(seta) == 1:
        scorea = 7
    if len(setb) == 1:
        scoreb = 7
    if len(seta) == 2:
        scorea = 6 if a.count(seta[0]) == 4 or a.count(seta[1]) == 4 else 5
    if len(setb) == 2:
        scoreb = 6 if b.count(setb[0]) == 4 or b.count(setb[1]) == 4 else 5
    if len(seta) == 3:
        occ = ''.join([str(a.count(x)) for x in seta])
        if occ.count('3') > 0:
            scorea = 4
        if occ.count('2') > 1:
            scorea = 3
    if len(setb) == 3:
        occ = ''.join([str(b.count(x)) for x in setb])
        if occ.count('3') > 0:
            scoreb = 4
        if occ.count('2') > 1:
            scoreb = 3
    if len(seta) == 4:
        scorea = 2
    if len(setb) == 4:
        scoreb = 2
    
    if part2:
        if a.count('J') == 4:
            scorea = 7
        if b.count('J') == 4:
            scoreb = 7
        if a.count('J') == 3:
            scorea = 7 if len(set([x for x in a if x != 'J'])) == 1 else 6
        if b.count('J') == 3:
            scoreb = 7 if len(set([x for x in b if x != 'J'])) == 1 else 6
        if a.count('J') == 2:
            if len(set([x for x in a if x != 'J'])) == 1:
                scorea = 7
            elif len(set([x for x in a if x != 'J'])) == 2:
                scorea = 6
            else:
                scorea = 4
        if b.count('J') == 2:
            if len(set([x for x in b if x != 'J'])) == 1:
                scoreb = 7
            elif len(set([x for x in b if x != 'J'])) == 2:
                scoreb = 6
            else:
                scoreb = 4
        if a.count('J') == 1:
            if len(set([x for x in a if x != 'J'])) == 1:
                scorea = 7
            elif len(set([x for x in a if x != 'J'])) == 2:
                if max([a.count(x) for x in a]) == 3:
                    scorea = 6
                else:
                    scorea = 5
            elif len(set([x for x in a if x != 'J'])) == 3:
                scorea = 4
            else:
                scorea = 2
        if b.count('J') == 1:
            if len(set([x for x in b if x != 'J'])) == 1:
                scoreb = 7
            elif len(set([x for x in b if x != 'J'])) == 2:
                if max([b.count(x) for x in b]) == 3:
                    scoreb = 6
                else:
                    scoreb = 5
            elif len(set([x for x in b if x != 'J'])) == 3:
                scoreb = 4
            else:
                scoreb = 2
            
    
    if scorea < scoreb:
        return -1
    if scorea == scoreb:
        for i in range(len(a)):
            if compare_chars[a[i]] == compare_chars[b[i]]:
                continue
            if compare_chars[a[i]] < compare_chars[b[i]]:
                return -1
            return 1
    return 0

lines = [i.strip().split() for i in stdin.read().splitlines()]
sortlines = sorted(lines, key=cmp_to_key(compare_cards))
compare_chars = {'2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'J': 0, 'Q': 11, 'K': 12, 'A': 13}
part2 = True
sortlines2 = sorted(lines, key=cmp_to_key(compare_cards))
solution = []
solution2 = []
for i in range(len(sortlines)):
    solution.append(int(sortlines[i][1])*(i+1))
for i in range(len(sortlines)):
    solution2.append(int(sortlines2[i][1])*(i+1))
print("Part 1:",sum(solution))
print("Part 2:",sum(solution2))
