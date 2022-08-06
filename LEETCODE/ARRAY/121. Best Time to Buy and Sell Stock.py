class Solution(object):
    def maxProfit(self, prices):
        minimum_price = max(prices)
        max_Profit = 0
        for i in range(0, len(prices)):
            if prices[i] < minimum_price:
                minimum_price = prices[i]
            else:
                if prices[i]-minimum_price > max_Profit:
                    max_Profit = prices[i]-minimum_price
        return max_Profit
                
        """
        :type prices: List[int]
        :rtype: int
        """
