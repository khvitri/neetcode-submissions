class Solution: 
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #   L       M           R
        # [-3, -3, -2, -1, 1, 2, 3, 4]

        nums.sort() # Ascending order

        res = []

        l = 0
        while l < len(nums) - 2:
            m, r = l + 1, len(nums) - 1
            
            while m < r:
                threeSum = nums[l] + nums[m] + nums[r]               

                if threeSum < 0:
                    m += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    res.append([nums[l], nums[m], nums[r]])
                    while m + 1 < len(nums) and nums[m] == nums[m + 1]:
                        m += 1
                    m += 1
            
            while l + 1 < len(nums) and nums[l] == nums[l + 1]:
                l += 1
            l += 1
        
        return res


        
