'''
Word Search II

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word
'''

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not words:
            return []
        
        self.build_trie(words)
        self.result = set()
        self.board = board
        self.m = len(board)
        self.n = len(board[0])
        
        for r, row in enumerate(self.board):
            for c, col in enumerate(row):
                self.dfs(r, c, self.trie)
                
        return list(self.result)
    
    def build_trie(self, words):
        self.trie = {}
        for word in words:
            curr_pos = self.trie
            for ch in word:
                if ch not in curr_pos:
                    curr_pos[ch] = {}
                curr_pos = curr_pos[ch]
            curr_pos['isWord'] = word
        
    def dfs(self, row, col, pos):
        ch = self.board[row][col]
        
        if ch not in pos:
            return
        
        pos = pos[ch]
        if 'isWord' in pos:
            self.result.add(pos['isWord'])
        
        self.board[row][col] = -1
        for cr, cc in self.getNeighbours(row, col, pos):
            self.dfs(cr, cc, pos)
        self.board[row][col] = ch
        
    def getNeighbours(self, row, col, pos):
        valid = []
        # UP
        if row > 0  and self.board[row - 1][col] in pos:
            valid.append((row - 1, col))
        # DOWN
        if row < self.m-1 and self.board[row + 1][col] in pos:
            valid.append((row + 1, col))
        # LEFT
        if col > 0  and self.board[row][col - 1] in pos:
            valid.append((row, col - 1))
        # RIGHT
        if col < self.n-1 and self.board[row][col + 1] in pos:
            valid.append((row, col + 1))
        
        return valid

#Runtime: 324 ms
#Memory Usage: 28 MB