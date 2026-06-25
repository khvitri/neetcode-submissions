class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        sumSet = []
        def dfs(i: int, total: int) -> None:
            if total == target:
                res.append(sumSet.copy())
                return

            if i >= len(nums) or total > target:
                return
                
            sumSet.append(nums[i])
            dfs(i, total + nums[i])

            sumSet.pop()
            dfs(i + 1, total)
            
        nums.sort()
        dfs(0, 0)
        return res


        