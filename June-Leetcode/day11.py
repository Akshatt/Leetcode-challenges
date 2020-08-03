'''

Sort Colors

Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.
'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        front_index = 0
        back_index = len(nums) - 1
        i = 0

        while i <= back_index: 

            if nums[i] == 0:

                nums[front_index], nums[i]  = nums[i], nums[front_index]
                front_index += 1
                i += 1

            elif nums[i] == 2:

                nums[i], nums[back_index] =nums[back_index], nums[i]
                back_index -= 1

            else:
                i += 1
    
#Runtime: 36 ms
#Memory Usage: 13.8 MB