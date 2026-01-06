class Solution(object):
    def maxProfit(self, prices):
        profit =0
        m = float('inf')
        for i in range(len(prices)):
            if prices[i] < m:
                m = prices[i]
            if prices[i] - m > profit:
                profit = prices[i] - m
        if profit > 0:
            return profit
        else:
            return 0            
        """
        :type prices: List[int]
        :rtype: int
        """
        