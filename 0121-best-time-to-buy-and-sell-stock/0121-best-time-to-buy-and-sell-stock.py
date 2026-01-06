class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        current_min = prices[0]
        if len(prices) == 1:
            return res
        for i in range(1,len(prices)):
            res = max(res, prices[i]-current_min)
            current_min = min(current_min, prices[i])
        return res