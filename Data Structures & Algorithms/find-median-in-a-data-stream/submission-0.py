class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)        

    def findMedian(self) -> float:
        self.arr.sort()
        mid = len(self.arr) // 2
        if len(self.arr) % 2:
            return self.arr[mid]
        else:
            return (self.arr[mid - 1] + self.arr[mid]) / 2
        