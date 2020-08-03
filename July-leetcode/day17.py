'''
Top K Frequent Elements

Given a non-empty array of integers, return the k most frequent elements.

'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [i for i,j in collections.Counter(nums).most_common(k)]
        

#Runtime: 188 ms
#Memory Usage: 18.5 MB