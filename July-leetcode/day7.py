'''
Island Perimeter

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
'''

class Solution:
    '''
    The approach is that first we assume that a 1 is not surrounded by other 1s and add 4 to the count. 
    Then we check the left and upper squares to see if it is 1. 
    If yes, then we subtract 2 from the count
    '''
    
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    count += 4
                    if j > 0 and grid[i][j - 1]:
                        count -= 2
                    if i > 0 and grid[i - 1][j]:
                        count -= 2
        return count

#Runtime: 756 ms
#Memory Usage: 14.1 MB