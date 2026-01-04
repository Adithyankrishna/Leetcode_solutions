class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1}
        summ = 0
        count = 0

        for num in nums:
            summ += num
            if summ - k in prefix:
                count += prefix[summ-k]
            prefix[summ] = prefix.get(summ,0)+1
        return count 
        