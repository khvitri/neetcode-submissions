class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Memo: Stores the minimum coins needed at n amount
        memo = [0]
        INF = float('inf')

        for amt in range(1, amount + 1):
            memo.append(INF)
            for coin in coins:
                if coin > amt:
                    continue
                memo[amt] = min(memo[amt], 1 + memo[amt - coin])
        
        return memo[amount] if memo[amount] != INF else -1
                

                    
