class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set() # Contains tuple of coords

        def isWord(i: int, j: int, subWord: str) -> bool:
            if not subWord: return True

            if i >= len(board) or i < 0 or j >= len(board[0]) or j < 0:
                return False
            
            if (i, j) in visited:
                return False
            
            if board[i][j] == subWord[0]:
                visited.add((i, j))
                newSubWord = subWord[1:]
                found = isWord(i - 1, j, newSubWord) or isWord(i, j + 1, newSubWord) or isWord(i + 1, j, newSubWord) or isWord(i, j - 1, newSubWord)
                visited.remove((i, j))
                return found
            
            return False
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if isWord(i, j, word):
                    return True
        
        return False
        





