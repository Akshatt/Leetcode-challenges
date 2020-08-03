'''
Course Schedule II

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

'''

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []

        def dfs_visit(s, adj, visited, visiting):
            visited.add(s)
            visiting.add(s)
            for v in adj[s]:
                if v in visiting:
                    return False
                elif v not in visited:
                    if not dfs_visit(v, adj, visited, visiting):
                        return False
            visiting.remove(s)
            res.append(s)
            return True
            
        def dfs(n, adj):
            visited = set()
            for v in range(n):
                if v not in visited:
                    if not dfs_visit(v, adj, visited, set()):
                        return False
            return True
        
        adj = defaultdict(list)
        for link in prerequisites:
            adj[link[1]].append(link[0])
        if not dfs(numCourses, adj):
            return []
        return reversed(res)

#Runtime: 152 ms
#Memory Usage: 16.7 MB