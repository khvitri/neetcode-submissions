class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # [3, 2, 1, 3]
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        
        return -1