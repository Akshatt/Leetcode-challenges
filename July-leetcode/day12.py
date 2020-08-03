'''
Reverse Bits

Reverse bits of a given 32 bits unsigned integer.
'''
class Solution:
    def reverseBits(self, n: int) -> int:
        a = bin(n)[2:][::-1]
        n = len(a)
        while n < 32:
            n +=1
            a += '0'
        return int(a,2)

#Runtime: 44 ms
#Memory Usage: 14 MB