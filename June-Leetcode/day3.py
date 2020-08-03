'''
Two City Scheduling


There are 2N people a company is planning to interview.
The cost of flying the i-th person to city A is costs[i][0],
and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.
'''





class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: x[0] - x[1])
        minCost, n = 0, len(costs)//2
        for i in range(n):
            minCost += costs[i][0]
        for i in range(n,2*n):
            minCost += costs[i][1]
        return minCost

#Runtime: 84 ms
#Memory Usage: 13.8 MB
