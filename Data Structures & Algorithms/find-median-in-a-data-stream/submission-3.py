class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        heapq.heapify(self.small)
        heapq.heapify(self.large)

    def addNum(self, num: int) -> None:
        if self.large and self.large[0] < num:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
        
        # Rebalance
        if len(self.large) > len(self.small) + 1:
            # Move large to small
            num = heapq.heappop(self.large)
            heapq.heappush(self.small, -num)
        elif len(self.small) > len(self.large) + 1:
            num = heapq.heappop(self.small)
            heapq.heappush(self.large, -num)

    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return self.large[0]
        elif len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return (-self.small[0] + self.large[0]) / 2
        