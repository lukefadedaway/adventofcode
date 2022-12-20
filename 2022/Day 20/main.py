import sys
nums = [(i, x) for i, x in enumerate([int(line) for line in sys.stdin])]
decrypted = nums.copy()
for i, x in nums:
    moveFrom = decrypted.index((i,x))
    decrypted.insert(((moveFrom + x)%(len(nums)-1)),decrypted.pop(moveFrom))
print("Part 1:\n",sum(decrypted[(([x[1] for x in decrypted].index(0))+offset)%len(nums)][1] for offset in [1000,2000,3000]))
decryptionkey = 811589153
decrypted2 = [(i, x*decryptionkey) for i, x in nums]
for _ in range(0,10):
    for i, x in nums:
        moveFrom = decrypted2.index((i,x*decryptionkey))
        decrypted2.insert(((moveFrom + x*decryptionkey)%(len(nums)-1)),decrypted2.pop(moveFrom))
print("Part 2:\n",sum(decrypted2[(([x[1] for x in decrypted2].index(0))+offset)%len(nums)][1] for offset in [1000,2000,3000]))