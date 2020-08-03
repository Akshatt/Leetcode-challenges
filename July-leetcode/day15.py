'''
Reverse Words in a String

Given an input string, reverse the string word by word.
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))

#Runtime: 40 ms
#Memory Usage: 14.5 MB