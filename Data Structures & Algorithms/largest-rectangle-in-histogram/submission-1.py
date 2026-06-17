class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxA = 0
        stack = [(0, heights[0])]

        for i in range(len(heights)):
            minIdx = i
            while stack and heights[i] < stack[-1][1]:
                top = stack.pop()
                maxA = max((top[1] * (i - top[0])), maxA)
                minIdx = top[0]
            stack.append((minIdx, heights[i]))
        
        for i, h in stack:
            maxA = max(h * (len(heights) - i), maxA)
        
        return maxA
        

            
                


            
