class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        sum_ = 0
        min_len = float('inf')

        for end in range(n):
            sum_ += nums[end]

            while sum_ >= target:
                min_len = min(min_len, end - start + 1)
                sum_ -= nums[start]
                start += 1

        return 0 if min_len == float('inf') else min_len