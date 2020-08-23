'''
Sort Array By Parity

Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.
'''
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return [i for i in A if i%2==0] + [i for i in A if i%2==1] 

#Runtime: 100 ms
#Memory Usage: 14.3 MB