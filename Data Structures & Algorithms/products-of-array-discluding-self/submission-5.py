class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        # Products from leftside of i, excluding i
        for i in range(1, len(nums)):
            output[i] = output[i - 1] * nums[i - 1]

        # Products from rightside of i, excluding i
        curProduct = 1
        for i in range(len(nums) - 2, -1, -1):
            curProduct *= nums[i + 1]
            output[i] *= curProduct
        
        return output

