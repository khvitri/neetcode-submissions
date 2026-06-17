class Solution:
    def trap(self, height: List[int]) -> int:
        # min(max height to the left, max height to the right) - height current cell 
        maxA = 0

        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i - 1], height[i - 1])
            maxRight[len(height) - 1 - i] = max(maxRight[len(height) - i], height[len(height) - i]) 
        
        for i in range(len(height)):
            curTrap = min(maxLeft[i], maxRight[i]) - height[i]
            maxA += max(curTrap, 0)
        
        return maxA
        
