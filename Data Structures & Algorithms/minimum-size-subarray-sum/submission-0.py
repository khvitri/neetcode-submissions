class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Sliding Window
        # minSubArrLen: 3
        # l: 3
        # r: 5
        # window: r - l + 1 = 3
        # winTotal = 9
        # [2,1,5,1,5,3]
        # target = 10

        minSubArrLen = 0
        winTotal = 0
        l = 0
        for r in range(len(nums)):
            winTotal += nums[r]
            while winTotal >= target:
                minSubArrLen = min(r - l + 1, minSubArrLen) if minSubArrLen != 0 else r - l + 1
                winTotal -= nums[l]
                l += 1
        
        return minSubArrLen

        