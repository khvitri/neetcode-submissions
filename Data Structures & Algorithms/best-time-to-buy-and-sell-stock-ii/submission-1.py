class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        for r in range(1, len(prices)):
            if prices[r] - prices[r - 1] > 0:
                maxP += prices[r] - prices[r - 1] 
        
        return maxP