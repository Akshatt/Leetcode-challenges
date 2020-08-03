'''
Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r = len(board)
        c = len(board[0])
        
        def isValid(i,j,idx, visited):
            if (i,j) in visited:
                return False

            # print(visited, idx)
            if idx == len(word):
                return True
            elif i<0 or i>=r or j<0 or j>=c:
                return False
            elif board[i][j] == word[idx]:
                return isValid(i+1, j, idx+1, visited+[(i,j)]) or isValid(i-1, j, idx+1,visited+[(i,j)]) or isValid(i, j+1, idx+1,visited+[(i,j)]) or isValid(i, j-1, idx+1,visited+[(i,j)])
            else:
                return False
        
        for i in range(r):
            for j in range(c):
                if board[i][j] == word[0]:
                    if isValid(i,j,0,[]): return True
        return False

#Runtime: 644 ms
#Memory Usage: 17.7 MB