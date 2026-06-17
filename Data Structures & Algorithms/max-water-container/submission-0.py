class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = min(heightL, heightR) * width
        # width = r - l
        # left pointer points to start element of the array
        # right pointer points to last element of the array
        # shift left pointer to the right if height[left] < height[right]
        # shift right pointer to the left if height[right] < height[left]
        # if height[left] = height[right], then default to shifting left
        # terminate when left == right
        # [20, 1, 20, 1, 7]
        #  7 * 5 = 35
        # 10 * 2 = 40

        l, r = 0, len(heights) - 1
        maxArea = min(heights[l], heights[r]) * (r - l)
        while l < r:
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
            
            curArea = min(heights[l], heights[r]) * (r - l)
            if curArea > maxArea:
                maxArea = curArea
        
        return maxArea

