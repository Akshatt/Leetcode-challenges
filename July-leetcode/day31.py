'''
Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        sol = [1,1]
        for i in range(2,n+1):
            sol.append(sol[i-1]+sol[i-2])
        return sol[n]
            

#Runtime: 40 ms
#Memory Usage: 13.7 MB