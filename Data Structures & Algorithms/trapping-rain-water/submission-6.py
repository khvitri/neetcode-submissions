class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        resultArr = [0] * len(height)

        for i in range(1, len(height)):
            maxLeft[i] = max(height[i - 1], maxLeft[i - 1])
        
        for i in range(len(height) - 2, 0, -1):
            print(i)
            maxRight[i] = max(height[i + 1], maxRight[i + 1])

        for i in range(len(height)):
            currWaterTrapped = min(maxLeft[i], maxRight[i]) - height[i]
            if currWaterTrapped > 0:
                resultArr[i] = currWaterTrapped
        print(resultArr) 
        return sum(resultArr)

