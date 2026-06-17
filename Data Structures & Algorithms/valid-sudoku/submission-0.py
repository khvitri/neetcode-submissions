class Solution:
    def _checkBox(self, board: List[List[str]], rowIdx: int, colIdx: int) -> bool:
        boxSize = 3
        seen = set()
        for boxRowIdx in range(rowIdx, rowIdx + boxSize):
            for boxColIdx in range(colIdx, colIdx + boxSize):
                num = board[boxRowIdx][boxColIdx]
                if num in seen and num != ".":
                    return False
                seen.add(num)
        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # First check the rows for duplicates
        for row in board:
            seen = set()
            for num in row:
                if num in seen and num != ".":
                    return False
                seen.add(num)

        # Then, check the columns for duplicates
        for colIdx in range(0, len(board[0])):
            seen = set() 
            for rowIdx in range(0, len(board)):
                num = board[rowIdx][colIdx]
                if num in seen and num != ".":
                    return False
                seen.add(num)

        # Finally, check the boxes for duplicates
        for rowIdx in range(0, len(board), 3):
            for colIdx in range(0, len(board[0]), 3):
                if not self._checkBox(board, rowIdx, colIdx):
                    return False

        return True