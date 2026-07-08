class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        minute = 0

        # Each rotten food gets its own queue containing
        # adjacent cells to it.
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotQ = deque([(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)])
                    q.append(rotQ)
                elif grid[r][c] == 1:
                    fresh += 1
        
        if not fresh: return 0
        
        while q:
            minute += 1
            for i in range(len(q)):
                rotQ = q.popleft()
                for j in range(len(rotQ)):
                    r, c = rotQ.popleft()
                    
                    if (r >= 0 and
                      c >= 0 and
                      r < ROWS and
                      c < COLS and
                      grid[r][c] == 1):
                        grid[r][c] = 2
                        fresh -= 1
                        rotQ.append((r - 1, c))
                        rotQ.append((r, c + 1))
                        rotQ.append((r + 1, c))
                        rotQ.append((r, c - 1))
                
                if rotQ: q.append(rotQ)
        
        return minute - 1 if not fresh else -1
                

