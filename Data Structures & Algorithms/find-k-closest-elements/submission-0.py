class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # x: 0
        # k: 5
        # | dif. x | = 1
        # l: 3
        # r: 3
        # [-3, -3, -2, -1, 1, 1, 1, 2, 4]
        # [-2, -1, 1, 1, 1]
        if k == 0: return []
        if k >= len(arr): return arr

        l = r = 0
        # Get the closest element
        while r < len(arr) - 1:
            if (abs(arr[r] - x) < abs(arr[r + 1] - x) or 
                (abs(arr[r] - x) == abs(arr[r + 1] - x) and arr[r] < arr[r + 1])):
                break            
            r += 1
        
        closestElem = deque([arr[r]])
        l = r
        # Decide to go left or right
        while len(closestElem) < k:
            if l > 0 and r >= len(arr) - 1:
                l -= 1
                closestElem.appendleft(arr[l])
                continue
            elif l <= 0 and r < len(arr) - 1:
                r += 1
                closestElem.append(arr[r])
                continue
            
            if abs(arr[r + 1] - x) < abs(arr[l - 1] - x):
                r += 1
                closestElem.append(arr[r])
            else:
                l -= 1
                closestElem.appendleft(arr[l])

        return list(closestElem)