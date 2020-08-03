'''
Longest Duplicate Substring

Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.  (The occurrences may overlap.)

Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated substring, the answer is "".)
'''

p = 2**63 - 1
class Solution:
    def longestDupSubstring(self, S):
        def rabin_karp(mid):
            cur_hash = 0
            for i in range(mid):
                cur_hash = (cur_hash * 26 + nums[i]) % p
            hashes = {cur_hash}
            pos = -1
            max_pow = pow(26, mid, p)
            for i in range(mid, len(S)):
                cur_hash = (26*cur_hash-nums[i-mid]*max_pow + nums[i]) % p
                if cur_hash in hashes:
                    pos = i + 1 - mid
                hashes.add(cur_hash)
            return pos


        low, high = 0, len(S)-1
        end = 0
        start = 0
        nums = [ord(c)-ord('a') for c in S]
        while low <= high:
            mid = (low+high) // 2
            pos = rabin_karp(mid)
            if pos == -1:  # no matching strings found
                high = mid - 1
            else:
                start = pos
                low = mid + 1
        return S[start:start+low-1]

#Runtime: 1592 ms
#Memory Usage: 26.6 MB