class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # A queue of BFS queues. A BFS starts when we encounter a 0. 
        # The BFS will be run in "parallel".

        ROWS, COLS = len(grid), len(grid[0])

        q = deque()
        distance = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    bfsQ = deque([(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)])
                    q.append(bfsQ)
                
        while q:
            distance += 1
            for i in range(len(q)):
                bfsQ = q.popleft()

                for j in range(len(bfsQ)):
                    r, c = bfsQ.popleft()
                    
                    if r >= 0 and c >= 0 and r < ROWS and c < COLS and grid[r][c] == 2147483647:
                        grid[r][c] = distance
                        bfsQ.append((r - 1, c))
                        bfsQ.append((r, c + 1))
                        bfsQ.append((r + 1, c))
                        bfsQ.append((r, c - 1))
                
                if bfsQ:
                    q.append(bfsQ)
                





