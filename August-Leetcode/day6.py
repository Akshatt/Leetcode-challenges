'''
Find All Duplicates in an Array

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?
'''
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        c=collections.Counter(nums)
        return [key for key in c if c[key]==2]

#Runtime: 440 ms
#Memory Usage: 22.3 MB