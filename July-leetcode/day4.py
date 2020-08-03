'''
Ugly Number II

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
'''
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i = j = k = 0
        count = 0
        
        while count < n:
            val = min(ugly[i]*2,min(ugly[j]*3, ugly[k]*5))
            if val == ugly[i]*2:
                i += 1
            if val == ugly[j]*3:
                j += 1
            if val == ugly[k]*5:
                k += 1
            count += 1
            if count == n:
                return ugly[-1]
            ugly.append(val)
        
#Runtime: 348 ms
#Memory Usage: 13.8 MB