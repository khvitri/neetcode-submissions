class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        sumSet = []
        exclude = set()

        def dfs(i: int, total: int) -> None:
            if total == target:
                res.append(sumSet.copy())
                return
            
            while i < len(candidates) and candidates[i] in exclude:
                i += 1
            

            if total > target or i >= len(candidates):
                return

            sumSet.append(candidates[i]) 
            dfs(i + 1, total + candidates[i])
            
            sumSet.pop()
            exclude.add(candidates[i])
            dfs(i + 1, total)
            exclude.remove(candidates[i])
        
        dfs(0, 0)
        return res
        