class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0

        def dfsArea(r: int, c: int) -> int:
            area = 0
            stack = [(r, c)]

            while stack:
                row, col = stack.pop()

                if (row < 0 or 
                  col < 0 or
                  row >= ROWS or
                  col >= COLS or
                  grid[row][col] == 0):
                    continue

                stack.append((row - 1, col))
                stack.append((row, col + 1))
                stack.append((row + 1, col))
                stack.append((row, col - 1))

                grid[row][col] = 0
                area += 1
            
            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res, dfsArea(r, c))
        
        return res

                
                


