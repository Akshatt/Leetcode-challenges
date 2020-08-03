'''
Queue Reconstruction by Height

Suppose you have a random list of people standing in a queue. 
Each person is described by a pair of integers (h, k), where h is the height of the person and 
k is the number of people in front of this person who have a height greater than or equal to h. 
Write an algorithm to reconstruct the queue.
'''


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        result=[]
        people.sort(key = lambda x:(-x[0],x[1]))
        for x,y in people:
            result.insert(y,[x,y])
        return result

#Runtime: 100 ms
#Memory Usage: 14.2 MB