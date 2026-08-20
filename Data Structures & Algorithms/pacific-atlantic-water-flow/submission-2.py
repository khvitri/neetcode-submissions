class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        movement = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        pacific, atlantic = set(), set()

        def dfs(r: int, c: int, pHeight: int, flow: set):
            if (r not in range(ROWS) or
              c not in range(COLS) or
              pHeight > heights[r][c] or
              (r, c) in flow):
                return
            
            flow.add((r, c))
            for dr, dc in movement:
                dfs(r + dr, c + dc, heights[r][c], flow)
        
        for r in range(ROWS):
            dfs(r, 0, -1, pacific)
            dfs(r, COLS - 1, -1, atlantic)
        
        for c in range(COLS):
            dfs(0, c, -1, pacific)
            dfs(ROWS - 1, c, -1, atlantic)
        
        return [[r, c] for r, c in pacific.intersection(atlantic)]
                

            