'''
Find Minimum in Rotated Sorted Array II

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        
        while left< right:
            mid = left + (right-left) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid if nums[right] != nums[mid] else right-1 
        return nums[left]
         

#Runtime: 48 ms
#Memory Usage: 14.3 MB