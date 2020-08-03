'''
Single Number II

Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

'''

from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        return list(c.keys())[list(c.values()).index(1)]
                
#Runtime: 60 ms
#Memory Usage: 15.6 MB