class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, quad = [], []

        def nSum(n, start, target):
            if n != 2:
                for i in range(start, len(nums) - n + 1):
                    if i > start and nums[i] == nums[i - 1]: continue
                    quad.append(nums[i])
                    nSum(n - 1, i + 1, target - nums[i])
                    quad.pop()
                return

            # base case, two sum II
            l, r = start, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append(quad + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        
        nSum(4, 0, target)
        return res
