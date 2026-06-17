class TimeValue:
    
    def __init__(self, timestamp: int, value: str):
        self.timestamp = timestamp
        self.value = value

class TimeMap:
    # Represent TimeMap as a dictionary
    # {
    #   key1: [(t1, val1), (t2, val2), ...], # Strictly increasing order by timestamp
    #   key2: [...],
    #   ... 
    # }
    # 
    # `set` is in strictly increasing order
    #   Add the (timestamp, value) to the end of the array at key
    #
    # `get`
    #   Binary search on [(t1, val1), (t2, val2), ...] to find the closest tx to timestamp
    #   where tx <= timestamp

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap:
            self.timeMap[key].append(TimeValue(timestamp, value))
        else:
            self.timeMap[key] = [TimeValue(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""

        vals = self.timeMap[key]
        l, r = 0, len(vals) - 1
        res = ""

        while l <= r:
            m = (l + r) // 2

            if vals[m].timestamp > timestamp:
                r = m - 1
            elif vals[m].timestamp < timestamp:
                l = m + 1
                res = vals[m].value
            else:
                return vals[m].value
        
        return res
            


