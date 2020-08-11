'''
Rotting Oranges

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.
'''
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        if rows == 0: return -1
        
        cols = len(grid[0])
        fresh, timer = 0, 0
        rotten = deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        while rotten and fresh > 0:
            timer += 1
            for _ in range(len(rotten)):
                x,y = rotten.popleft()

                for dx,dy in [(0,1), (1,0), (0,-1), (-1,0)]:
                    nx, ny = x+dx, y + dy

                    if nx < 0 or nx == rows or ny <0 or ny == cols:
                        continue
                    if grid[nx][ny] == 0 or grid[nx][ny] == 2:
                        continue

                    fresh -= 1
                    grid[nx][ny] = 2
                    rotten.append((nx,ny))

        return timer if fresh == 0 else -1
        
                    
#Runtime: 48 ms
#Memory Usage: 13.8 MB