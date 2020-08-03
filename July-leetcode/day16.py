'''
Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n.
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if abs(x) < 1e-40: return 0 
        if n == 0: return 1
        if n < 0: return self.myPow(1/x, -n)
        lower = self.myPow(x, n//2)
        if n % 2 == 0: return lower*lower
        if n % 2 == 1: return lower*lower*x
        

#Runtime: 52 ms
#Memory Usage: 14 MB