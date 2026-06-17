class MinStack:

    def __init__(self):
        self.dq = deque([])
        self.stack = []        

    def push(self, val: int) -> None:
        self.stack.append(val)        
        if self.dq and self.dq[0] >= val:
            self.dq.appendleft(val)
        else:
            self.dq.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val > self.dq[0]:
            self.dq.pop()
        else:
            self.dq.popleft()

    def top(self) -> int:
        return self.stack[-1]        

    def getMin(self) -> int:
        return self.dq[0]

        
