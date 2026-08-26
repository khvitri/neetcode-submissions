class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(total: int) -> float:
            if total == amount:
                return 0
            if total > amount:
                return float('inf')
            if total in memo:
                return memo[total]
            
            res = float('inf')
            for coin in coins:
                res = min(res, 1 + dfs(total + coin))
            
            memo[total] = res
            return res

        ans = dfs(0)
        return int(ans) if ans != float('inf') else -1