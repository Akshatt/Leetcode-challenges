'''
Single Number III

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = []
        count = collections.Counter(nums)
        for k,v in count.items():
            if v == 1:
                res.append(k)
        return res


#Runtime: 56 ms
#Memory Usage: 15.6 MB