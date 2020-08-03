'''
Word Break II

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
'''
class Solution:
    
    def __init__(self):
        self.saved = {}

    def wordBreak(self, s, dict):
        self.saved.clear()
        size = len(s)
        return self.wordBreakImpl(s, dict)

    def wordBreakImpl(self, s, dict):
        if s in self.saved:
            return self.saved[s]
        else:
            ret = []
        for i in range(0, len(s)):
            subs = s[0:i+1]
            if subs in dict:
                if (i + 1) == len(s):
                    currResult = [s]
                else:
                    sentences = self.wordBreakImpl(s[i+1:], dict)
                    currResult = map(lambda s: subs + " " + s, sentences)
                ret += currResult

        self.saved[s] = ret
        return ret

#Runtime: 184 ms
#Memory Usage: 14.2 MB