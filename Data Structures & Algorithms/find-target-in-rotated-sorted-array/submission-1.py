class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # If rotated, two portions: left and right
        #   All nums. in left portion is greater than right portion
        #   l: leftmost of left portion
        #   r: rightmost of right portion

        #   If m in right & r > target & m < target, l = m + 1
        #   If m in left & l < target & m < target, l = m + 1
        #   If m in left & l > target, l = m + 1

        #   If m in left & l < target & m > target, r = m - 1
        #   If m in right & r > target & m > target, r = m - 1
        #   If m in right & r < target, r = m - 1 

        #  l           m  r  
        # [3, 4, 5, 6, 1, 2]
        # m = 2
        # l = 0
        # r = 5
        # t = 6

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            inLeft = nums[m] >= nums[l]
            inRight = not inLeft

            if nums[m] == target:
                return m
            elif nums[l] == target:
                return l
            elif nums[r] == target:
                return r

            if (inRight and nums[r] > target and nums[m] < target) or (inLeft and nums[l] < target and nums[m] < target) or (inLeft and nums[l] > target):
                l = m + 1
            elif (inLeft and nums[l] < target and nums[m] > target) or (inRight and nums[r] > target and nums[m] > target) or (inRight and nums[r] < target):
                r = m - 1
        
        return -1
            


