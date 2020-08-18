'''
Numbers With Same Consecutive Differences

Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.

Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.
'''
class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        @lru_cache(None)
        def dfs(i,j):
            if j < 0 or j > 9 or (j == 0 and i == 1): return []
            if i == 1: return [str(j)]
            dirs, out = set([K, -K]), []
            for d in dirs:
                out += [s+str(j) for s in dfs(i-1,j+d)]
            return out
        
        if N == 1: return range(10)
        return list(chain(*[dfs(N, i) for i in range(10)]))
    

#Runtime: 28 ms
#Memory Usage: 14.1 MB