class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 , rob2 = 0 , 0 
        for house in nums:
            money = max(house+ rob1, rob2)
            rob1 = rob2
            rob2 = money
        return rob2
        