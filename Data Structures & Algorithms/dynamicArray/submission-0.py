class DynamicArray:
    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.arr = [None] * self.cap
        self.size = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if not self.arr[i]:
            raise Exception("index out of range")
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size >= self.cap:
            self.resize()
        self.arr[self.size] = n        
        self.size += 1

    def popback(self) -> int:
        res = self.arr[self.size - 1]
        self.arr[self.size - 1] = None
        self.size -= 1
        return res

    def resize(self) -> None:
        self.arr = self.arr + [None] * self.cap
        self.cap = self.cap * 2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.cap
