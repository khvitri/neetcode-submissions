class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [0] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i, len(nums)):
                lis[i] = max(1 + lis[j] if nums[i] < nums[j] else 1, lis[i])
        
        return max(lis)