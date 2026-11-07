class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        memo = [[-1] * (target + 1) for _ in range(len(nums))]

        def dfs(index, target):
            if target == 0:
                return True
            
            if (target < 0 or
                index >= len(nums)):
                return False
            
            if memo[index][target] != -1:
                return memo[index][target]

            # Include current number or not
            memo[index][target] = (dfs(index + 1, target - nums[index]) or
                dfs(index + 1, target))
            
            return memo[index][target]
        
        return dfs(0, target)
            

            