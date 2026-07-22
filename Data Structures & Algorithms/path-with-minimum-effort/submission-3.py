class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights) - 1, len(heights[0]) - 1
        TARGET = (ROWS, COLS)

        visited = set()
        minHeap = [[0, 0, 0]] # effor, r, c
        moves = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        def bfs() -> int:
            while minHeap:
                maxEffort, r, c = heapq.heappop(minHeap)

                if (r, c) in visited:
                    continue

                if (r, c) == TARGET:
                    return maxEffort
                
                visited.add((r, c))
                for dr, dc in moves:
                    nr, nc = r + dr, c + dc
                    if (nr in range(ROWS + 1) and
                      nc in range(COLS + 1) and
                      (nr, nc) not in visited):
                        effort = abs(heights[r][c] - heights[nr][nc])
                        heapq.heappush(minHeap, [max(effort, maxEffort), nr, nc])          

            return -1

        return bfs()


            