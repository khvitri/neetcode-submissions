class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Min-heap stores (distance, index to points)
        minHeapPoints = []
        heapq.heapify(minHeapPoints)

        for i, point in enumerate(points):
            distance = pow(point[0] - 0, 2) + pow(point[1] - 0, 2)

            heapq.heappush(minHeapPoints, (-distance, i))

            if len(minHeapPoints) > k:
                heapq.heappop(minHeapPoints)


        return [points[i] for d, i in minHeapPoints]