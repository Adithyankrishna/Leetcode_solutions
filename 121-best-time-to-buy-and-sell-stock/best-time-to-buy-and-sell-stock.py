class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        profit = 0
        maxv = 0

        while right < len(prices):
            if prices[right] - prices[left] > 0:
                profit = prices[right] - prices[left]
                maxv = max(profit,maxv)
                right+=1
            else:
                left = right
                right+=1
        return maxv
        