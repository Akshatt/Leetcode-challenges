'''
Pascal's Triangle II

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.
'''
class Solution:
    def getRow(self, rowIndex: int) -> List[int]: 
        if rowIndex == 0:
            return [1] 
        final = [1,1] 
        for i in range(0,rowIndex-1):
            final = [1] +[final[j]+final[j+1] for j in range(len(final)-1)] + [1]
        return final   

#Runtime: 32 ms
#Memory Usage: 14 MB