class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        minLeft = [0] * len(prices)
        maxRight = [0] * len(prices)
        minLeft[0] = prices[0]
        maxRight[-1] = prices[-1] 
        
        for i in range(1, len(prices)):
            if prices[i] < minLeft[i - 1]:
                minLeft[i] = prices[i] 
            else:
                minLeft[i] = minLeft[i - 1]
            
            if prices[len(prices) - i - 1] > maxRight[len(prices) - i]:
                maxRight[len(prices) - i - 1] = prices[len(prices) - i - 1] 
            else:
                maxRight[len(prices) - i - 1] = maxRight[len(prices) - i]

        print(maxRight)
        print(minLeft)
        maxProfit = 0
        for i in range(len(prices)):
            maxProfit = max(maxProfit, maxRight[i] - minLeft[i])
        
        return maxProfit

            
