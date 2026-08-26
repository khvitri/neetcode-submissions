class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        gp, sp = [nums[0]], [nums[0]]

        for i in range(1, len(nums)):
            gp.append(max(gp[i - 1] * nums[i], sp[i - 1] * nums[i], nums[i])) 
            sp.append(min(gp[i - 1] * nums[i], sp[i - 1] * nums[i], nums[i]))

            res = max(gp[-1], res)
        
        return res


