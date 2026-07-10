class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        noTouch = set()
        visit = set()

        def dfs(r: int, c: int) -> None:
            if (r in range(ROWS) and
              c in range(COLS) and
              board[r][c] == "O" and
              (r, c) not in visit):
                noTouch.add((r, c))
                visit.add((r, c))
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r + 1, c)
                dfs(r, c - 1) 
            
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)
        
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in noTouch:
                    board[r][c] = "X"
        

        

            


