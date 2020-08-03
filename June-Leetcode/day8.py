'''
Power of Two

Given an integer, write a function to determine if it is a power of two.
'''


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0: return False
        while n%2==0:
            n //= 2
        return n==1
#Runtime: 28 ms
#Memory Usage: 13.8 MB