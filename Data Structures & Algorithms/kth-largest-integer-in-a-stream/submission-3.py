class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = list(nums)
        heapq.heapify(self.minHeap)  # O(n)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        if self.minHeap and val <= self.minHeap[0]:
            return self.minHeap[0]
        
        if len(self.minHeap) == self.k:
            heapq.heappop(self.minHeap)

        heapq.heappush(self.minHeap, val)
        return self.minHeap[0]
