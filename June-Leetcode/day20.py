'''
Permutation Sequence

The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.
'''
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = ''
        nums = [i for i in range(1,n+1)]
        for i in range(n-1,0,-1):
            base = math.factorial(i)
            current = 0
            while k > base:
                k -= base
                current += 1
            res += str(nums[current])
            nums.pop(current)
        res += str(nums[0])
        return res

#Runtime: 32 ms
#Memory Usage: 13.9 MB