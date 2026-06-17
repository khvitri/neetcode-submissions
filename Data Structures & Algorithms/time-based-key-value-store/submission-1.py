class TimeVal:

    def __init__(self, value, timestamp):
        self.value = value
        self.timestamp = timestamp

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append(TimeVal(value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # Binary search over the list of timestamps
        if key in self.store:
            vals = self.store[key]

            bestVal = None
            l, r = 0, len(vals) - 1
            while l <= r:
                m = (l + r) // 2

                if vals[m].timestamp > timestamp:
                    r = m - 1
                elif vals[m].timestamp < timestamp:
                    l = m + 1
                    bestVal = vals[m].value
                else:
                    return vals[m].value
            
            if bestVal:
                return bestVal

        return ""

        
