class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        positions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        res = []

        # Look for cells able to flow to oceans
        def dfs(r: int, c: int, visit: set, prevHeight: int) -> None:
            if (r in range(ROWS) and
              c in range(COLS) and
              (r, c) not in visit and
              heights[r][c] >= prevHeight):
                visit.add((r, c))
                for dr, dc in positions:
                    dfs(r + dr, c + dc, visit, heights[r][c])
        
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        for cord in pac:
            if cord in atl:
                r, c = cord
                res.append([r, c])
        
        return res


                     


            


