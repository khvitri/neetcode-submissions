class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []

        nextGreater = {} # element in nums2: next greater in nums2

        for n2 in nums2:
            while stack and n2 > stack[-1]:
                val = stack.pop()
                nextGreater[val] = n2
            
            stack.append(n2)
        
        res = []
        for n1 in nums1:
            if n1 in nextGreater:
                res.append(nextGreater[n1])
            else:
                res.append(-1)
        
        return res