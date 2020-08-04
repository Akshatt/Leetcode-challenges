'''
Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = [i for i in s.lower() if i.isalnum()]
        return ns == ns[::-1] 
        

#Runtime: 32 ms
#Memory Usage: 15 MB