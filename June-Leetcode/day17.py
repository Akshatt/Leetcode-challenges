'''
Surrounded Regions

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
'''
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board) 
        n = len(board[0]) if m>0 else 0 
        def dfs(i,j):                              
            if board[i][j] == "O":
                board[i][j] = 'temp'
                for x , y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    if 0<=x<m and 0<=y<n:
                        dfs(x,y) 
        
        # for vertical borders
        for i in range(m):
            dfs(i,0)
            dfs(i,n-1)
        
        # for horizontal borders
        for i in range(1,n-1):
            dfs(0 ,i)
            dfs(m-1 ,i)
            
        for i in range(m):
            for j in range(n):
                if board[i][j]== 'temp' :
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"

#Runtime: 140 ms
#Memory Usage: 15.7 MB