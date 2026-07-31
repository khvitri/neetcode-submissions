class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        minHeap = [(0, points[0][0], points[0][1])] # cost, x, y

        totalCost = 0

        while minHeap:
            cost, x, y = heapq.heappop(minHeap)

            if (x, y) in visited:
                continue

            visited.add((x, y))
            totalCost += cost
            for xj, yj in points:
                if (xj, yj) in visited:
                    continue
                costj = abs(x - xj) + abs(y - yj)
                heapq.heappush(minHeap, (costj, xj, yj))
        
        return totalCost
                
                


        
