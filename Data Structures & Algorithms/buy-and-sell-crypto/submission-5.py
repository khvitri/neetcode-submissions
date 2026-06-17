class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l = 0
        for r in range(1, len(prices)):
            maxP = max(prices[r] - prices[l], maxP) 
            if prices[l] > prices[r]:
                l = r
        
        return maxP
        


        