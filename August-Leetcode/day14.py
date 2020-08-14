'''
Longest Palindrome

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.
'''
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        l = len(s)
        if l == 0 or l == 1: return l
        count = Counter(s)
        num,flag = 0,0
        for value in count.values():
            if value%2 == 0:
                num += value
            else:
                flag = 1
                num += (value-1)
        return num + flag 

#Runtime: 28 ms
#Memory Usage: 13.5 MB