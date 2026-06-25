class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        numSet = set(nums)

        perm = []
        def dfs() -> None:
            if not numSet:
                res.append(perm.copy())
                return

            for num in nums:
                if num in numSet:
                    perm.append(num)
                    numSet.remove(num)
                    dfs()
                    perm.pop()
                    numSet.add(num)

        dfs() 
        return res