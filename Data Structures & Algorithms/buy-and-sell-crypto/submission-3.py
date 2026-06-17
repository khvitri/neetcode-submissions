class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        l, r = 0, 1
        maxProfit = 0
        minValue = prices[l]
        while l < r and r < len(prices):
            if prices[r] < minValue:
                minValue = prices[r]
                l = r
                r += 1
            else:
                maxProfit = max(maxProfit, prices[r] - minValue)
                r += 1

        return maxProfit

            
