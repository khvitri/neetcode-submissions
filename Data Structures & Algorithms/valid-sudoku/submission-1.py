class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set) 
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board)):
                boxIdx = (row // 3, col // 3)
                if (board[row][col] in rows[row] or
                    board[row][col] in cols[col] or
                    board[row][col] in boxes[boxIdx]):
                    return False

                if board[row][col] != ".":
                    rows[row].add(board[row][col])
                    cols[col].add(board[row][col])
                    boxes[boxIdx].add(board[row][col])
        
        return True
