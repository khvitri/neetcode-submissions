class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islandNo = 0
        ROWS, COLS = len(grid), len(grid[0])

        visited = set()
        def scanIsland(r, c) -> None:
            if (r < 0 or 
              c < 0 or 
              r >= ROWS or 
              c >= COLS or 
              (r, c) in visited or 
              grid[r][c] != "1"):
                return
            
            if grid[r][c] == "1":
                visited.add((r, c))
                scanIsland(r - 1, c)
                scanIsland(r, c + 1)
                scanIsland(r + 1, c)
                scanIsland(r, c - 1)

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row, col) not in visited:
                    scanIsland(row, col)
                    islandNo += 1
        
        return islandNo
