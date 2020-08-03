'''
Cheapest Flights Within K Stops

There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.
'''

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        pq, g = [(0,src,K+1)], collections.defaultdict(dict)
        for s,d,w in flights: 
            g[s][d] = w
        while pq:
            cost, s, k = heapq.heappop(pq)
            if s == dst: 
                return cost
            if not k: continue
            for d in g[s]:
                heapq.heappush(pq, (cost+g[s][d], d, k-1))
        return -1

        
#Runtime: 104 ms
#Memory Usage: 19.5 MB