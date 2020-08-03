'''
Random Pick with Weight

Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
'''

import random

class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        total = sum(w)
        for i in range(len(w)):
            w[i] = w[i]/total
        for i in range(1,len(w)):
            w[i] += w[i-1]

    def pickIndex(self) -> int:
        N = random.uniform(0,1)
        index = -1
        
        while True:
            index += 1
            if N <= self.w[index]:
                return index


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


#Runtime: 8908 ms
#Memory Usage: 18.3 MB