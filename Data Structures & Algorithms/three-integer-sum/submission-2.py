class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        TARGET = 0
        res = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i != 0 and nums[i] == nums[i - 1]: continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == TARGET:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l - 1] == nums[l] and l < r:
                        l += 1
                elif total > TARGET:
                    r -= 1
                else:
                    l += 1
        
        return res
                

            