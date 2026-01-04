class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = {0:1}
        current = 0

        for  num in nums:
            current += num
            if (current - k) in prefix:
                count += prefix[current - k] 
            prefix[current] = prefix.get(current,0)+1
        return count
        