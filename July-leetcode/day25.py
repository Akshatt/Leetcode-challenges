'''
Add Digits

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
'''
class Solution:
    def addDigits(self, num: int) -> int:
        q = []
        while num != 0:
                q.append(num%10)
                num = num// 10
        temp = sum(q)
        if temp > 9:
            return self.addDigits(temp)  
        else:
            return temp


#Runtime: 28 ms
#Memory Usage: 13.8 MB