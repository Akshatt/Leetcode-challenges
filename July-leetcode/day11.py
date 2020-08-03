'''
Subsets

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(2**len(nums)): # all numbers described above
            subset = []
            for j, b in enumerate(f"{i:0{len(nums)}b}"):
                if b=="1": subset.append(nums[j])
            ans.append(subset)
        return ans

#Runtime: 52 ms
#Memory Usage: 14 MB