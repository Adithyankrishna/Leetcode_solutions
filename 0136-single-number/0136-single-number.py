class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        n = 0
        for i in range(len(nums)):
            n = n^nums[i]
        return n


        