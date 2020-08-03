'''
Hamming Distance

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.
'''
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a, b = bin(x)[2:], bin(y)[2:]
        diff = len(a)-len(b)
        count = 0
        if diff > 0:
            b = "0"*diff + b 
        elif diff <0:
            a = "0"*(-diff) + a
        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1
        return count
                
        
#Runtime: 48 ms
#Memory Usage: 13.7 MB