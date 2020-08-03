'''
H-Index II

Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

'''
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = len(citations)
        left, right = 0, l-1
        h = 0
        while right >= left:
            mid = (left + right) //2 
            if citations[mid] >= l-mid:
                h =  max(h, l-mid)
                right = mid - 1
            else:
                left = mid + 1
        return h


#Runtime: 152 ms
#Memory Usage: 20.5 MB