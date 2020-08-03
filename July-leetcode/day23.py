'''
All Paths From Source to Target

Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists
'''

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        q = [[0]]
        result = []
        target = len(graph) - 1        
        while q:
            temp = q.pop(0)
                
            if temp[-1] == target:
                result.append(temp)
            else:
                for neighbor in graph[temp[-1]]: 
                    q.append(temp + [neighbor])

        return result

#Runtime: 108 ms
#Memory Usage: 15.2 MB