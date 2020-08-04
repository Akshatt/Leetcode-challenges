'''
Power of Four

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
'''
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        while num > 1:
            num = num / 4
        if num == 1:
            return True
        else:
            return False
            

#Runtime: 24 ms
#Memory Usage: 13.8 MB