'''
Task Scheduler

Solution
You are given a char array representing tasks CPU need to do. It contains capital letters A to Z where each letter represents a different task. Tasks could be done without the original order of the array. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

You need to return the least number of units of times that the CPU will take to finish all the given tasks.
'''
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = list(collections.Counter(tasks).values())
        l = len(tasks)
        
        if not n: return l
        
        max_val = max(task_count)
        count_max_val = task_count.count(max_val)
        
        return max(l, (max_val-1)*(n+1) + count_max_val)
                
#Runtime: 444 ms
#Memory Usage: 14.1 MB