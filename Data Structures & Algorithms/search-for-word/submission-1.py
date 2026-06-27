class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set() # Contains tuple of coords

        def isWord(i: int, j: int, wordIdx: int) -> bool:
            if wordIdx >= len(word): return True

            if i >= len(board) or i < 0 or j >= len(board[0]) or j < 0:
                return False
            
            if (i, j) in visited:
                return False
            
            if board[i][j] == word[wordIdx]:
                visited.add((i, j))
                found = isWord(i - 1, j, wordIdx + 1) or isWord(i, j + 1, wordIdx + 1) or isWord(i + 1, j, wordIdx + 1) or isWord(i, j - 1, wordIdx + 1)
                visited.remove((i, j))
                return found
            
            return False
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if isWord(i, j, 0):
                    return True
        
        return False
        





