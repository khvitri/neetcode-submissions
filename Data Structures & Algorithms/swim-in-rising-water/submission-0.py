class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        movements = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        visit = set()
        minHeap = [(grid[0][0], 0, 0)] # time, r, c

        while minHeap:
            time, r, c = heapq.heappop(minHeap)

            if r == ROWS - 1 and c == COLS - 1:
                return time

            if (r, c) in visit:
                continue
            
            visit.add((r, c))
            for dr, dc in movements:
                nr, nc = r + dr, c + dc
                if (nr in range(ROWS) and
                  nc in range(COLS) and
                  (nr, nc) not in visit):
                    heapq.heappush(minHeap, (max(time, grid[nr][nc]), nr, nc))
        
        return -1
        
        
                

            

                

            

        

        
