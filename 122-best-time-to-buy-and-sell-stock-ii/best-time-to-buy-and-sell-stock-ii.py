class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        result =[0]*len(prices)
        profit = 0
        maxprofit = float('-inf')
        for i in range(len(prices)-1):
            result[i] = prices[i+1] -prices[i]
        for i in range(len(result)-1):
            if result[i] > 0:
                profit += result[i]
        return profit

        


        