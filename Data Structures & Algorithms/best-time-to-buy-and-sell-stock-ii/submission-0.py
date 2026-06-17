class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l = 0
        for r in range(1, len(prices)):
            if prices[r] - prices[l] > 0:
                maxP += prices[r] - prices[l] 
            l += 1
        
        return maxP