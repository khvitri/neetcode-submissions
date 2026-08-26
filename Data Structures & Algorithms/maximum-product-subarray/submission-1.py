class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        gp, sp = [nums[0] if nums[0] else 1], [nums[0] if nums[0] else 1]

        for i in range(1, len(nums)):
            if not nums[i]:
                gp.append(1)
                sp.append(1)
                res = max(0, res)
                continue

            gp.append(max(gp[i - 1] * nums[i], sp[i - 1] * nums[i], nums[i])) 
            sp.append(min(gp[i - 1] * nums[i], sp[i - 1] * nums[i], nums[i]))

            res = max(gp[-1], res)
        
        return res


