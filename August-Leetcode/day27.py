'''
 Find Right Interval

Given a set of intervals, for each of the interval i, check if there exists an interval j whose start point is bigger than or equal to the end point of the interval i, which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index, which means that the interval j has the minimum start point to build the "right" relationship for interval i. If the interval j doesn't exist, store -1 for the interval i. Finally, you need output the stored value of each interval as an array.

Note:

You may assume the interval's end point is always bigger than its start point.
You may assume none of these intervals have the same start point.
'''
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start_idx = {}
        for i, (start, end) in enumerate(intervals):
            start_idx[start] = i
        
        sorted_starts = sorted(list(start_idx.keys()))
        
        output = []
        for start, end in intervals:
            if end in start_idx:
                output.append(start_idx[end])
            else:
                idx = bisect.bisect_right(sorted_starts, end)
                if idx == len(sorted_starts):
                    output.append(-1)
                else:
                    min_right = sorted_starts[idx]
                    output.append(start_idx[min_right])
        return output

    

#Runtime: 280 ms
#Memory Usage: 19.4 MB