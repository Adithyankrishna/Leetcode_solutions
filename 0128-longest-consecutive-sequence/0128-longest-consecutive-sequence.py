class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxcount = 0

        for num in nums:
            if num + 1 not in seen:
                curr = num
                count = 0
                while curr in seen:
                    count += 1
                    curr -= 1
                maxcount = max(maxcount, count)

        return maxcount
