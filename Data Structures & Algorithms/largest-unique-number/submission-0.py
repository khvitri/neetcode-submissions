class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        notUnique = set()
        unique = set()

        for num in nums:
            if num in notUnique:
                continue
            
            if num in unique:
                unique.remove(num)
                notUnique.add(num)
            else:
                unique.add(num)
        
        res = -1
        for num in unique:
            res = max(num, res)
        
        return res


                