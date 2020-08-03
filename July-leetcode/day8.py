'''
3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums is None or len(nums)==0:return []
        
        res = set()
        nums.sort()
        l = len(nums)
        for i in range(l-2):
            j, k = i + 1, l-1
            while j < k :
                if (nums[i]+nums[j]+nums[k]>0):
                    k -= 1
                elif (nums[i] + nums[j]+nums[k]<0):
                    j += 1
                else:
                    res.add((nums[i], nums[j], nums[k]))     
                    j += 1
                    k -= 1
        return res
            
                    

#Runtime: 2388 ms
#Memory Usage: 17 MB

