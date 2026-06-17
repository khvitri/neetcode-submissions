class Solution:
    def findMin(self, nums: List[int]) -> int:
        # If nums[m] < nums[l], then we know m is in the right sorted portion
        # If nums[m] >= nums[l], then we know m is in the left sorted portion
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2

            if nums[l] <= nums[r]:
                return nums[l]

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m

        return nums[l]
