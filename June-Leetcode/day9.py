'''
Is Subsequence

Given a string s and a string t, check if s is subsequence of t.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not)
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        m, n = len(s), len(t)
        while i < m and j<n:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i==m


#Runtime: 28 ms
#Memory Usage: 13.9 MB