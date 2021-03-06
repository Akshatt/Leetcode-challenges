'''
Arranging Coins

You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.
'''
class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n <=1 :
            return n 
        i = 0
        while n>i:
            i += 1
            n -= i
        return i
             
        
#Runtime: 904 ms
#Memory Usage: 13.8 MB