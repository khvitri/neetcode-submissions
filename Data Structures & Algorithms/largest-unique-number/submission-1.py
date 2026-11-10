class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        seen = set()
        dups = set()
        for n in nums:
            if n not in seen:
                seen.add(n)
            elif n in seen:
                dups.add(n)

        res = -1 
        for n in nums:
            if n in dups:
                continue
            res = max(n, res)
        
        return res
