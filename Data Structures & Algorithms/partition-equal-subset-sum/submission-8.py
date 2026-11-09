class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        sums = {0}
        for n in nums:
            temp = set()
            for t in sums:
                if t == target or n + t == target:
                    return True
                temp.add(n + t)
            
            for t in temp:
                sums.add(t)

        return False