'''
Search Insert Position

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target <= nums[-1]:
            for i in range(len(nums)):
                if target > nums[i]:
                    continue
                else:
                    return i
        return len(nums)


#Runtime: 52 ms
#Memory Usage: 14.3 MB