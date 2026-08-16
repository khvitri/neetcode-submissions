class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        def swap(i, j) -> None:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        def reverse(l, r) -> None:
            while l < r:
                swap(l, r)
                l, r = l + 1, r - 1
        
        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums) - 1)
        

