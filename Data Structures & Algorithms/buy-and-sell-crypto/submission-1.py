class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window problem
        # differences between smallest and largest value
        # only shift left when it's bigger than right
        # right moves regardless
        # save biggest profit in maxProfit variable
        # compare to currentProfit

        l, r = 0, 1
        r = 1
        maxProfit, currentProfit = 0, 0
        while r in range(len(prices)):
            currentProfit = prices[r] - prices[l]
            maxProfit = max(maxProfit, currentProfit)
            if prices[r] < prices[l]:
                l=r
            r=r+1
            
        return maxProfit
            



