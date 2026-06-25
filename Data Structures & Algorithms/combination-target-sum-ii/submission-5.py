class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        sumSet = []
        def dfs(i: int, total: int) -> None:
            if total == target:
                res.append(sumSet.copy())
                return

            if total > target or i >= len(candidates):
                return
            
            if total + candidates[i] > target:
                return

            sumSet.append(candidates[i]) 
            dfs(i + 1, total + candidates[i])     
            sumSet.pop()
            
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, total)
        
        dfs(0, 0)
        return res
        