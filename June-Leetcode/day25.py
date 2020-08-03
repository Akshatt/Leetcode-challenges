'''
Find the Duplicate Number

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one
'''

from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for key, value in Counter(nums).items():
            if value > 1:
                return key
                
#Runtime: 68 ms
#Memory Usage: 17.1 MB