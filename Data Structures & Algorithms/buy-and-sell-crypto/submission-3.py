class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #two pointers(sliding window)
        #l only switches when r is smaller
        #r iterates till end of array
        #one variable to store highest and another for current
        #

        l,r =0,1

        biggestProfit = 0
        for r in range(len(prices)):
            currentProfit = prices[r]-prices[l]
            biggestProfit = max(currentProfit, biggestProfit)

            if prices[l]>=prices[r]:
                l = r

            r +=1
        return biggestProfit
