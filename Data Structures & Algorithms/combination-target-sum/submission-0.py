class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        sumSet = []
        def dfs(i: int) -> None:
            for idx in range(i, len(nums)):
                if sum(sumSet) < target:
                    sumSet.append(nums[idx])
                    dfs(idx)
                    sumSet.pop()
                elif sum(sumSet) > target:
                    return
                else:
                    res.append(sumSet.copy())
                    return
        
        dfs(0)
        return res


        