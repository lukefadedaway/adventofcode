import sys
import math
import functools

def compareLists(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return 0 if a == b else (-1 if a < b else 1)
    if isinstance(a,int):
        a = [a]
    if isinstance(b,int):
        b = [b]
    return ([compareLists(*x) for x in zip(a,b) if compareLists(*x) != 0] + [compareLists(len(a),len(b))])[0]


list_ = [eval(item) for item in [line.strip() for line in sys.stdin] if item != '']
print("Part 1:")
print(sum(i for i, x in enumerate(zip(list_[::2], list_[1::2]),1) if compareLists(*x) <= 0))
listvalid = sorted(list_ + [[[2]],[[6]]], key=functools.cmp_to_key(compareLists))
print("Part 2:")
print((listvalid.index([[2]])+1)*(listvalid.index([[6]])+1))