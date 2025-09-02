class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        inf =float('inf')
        for i in range(len(nums)):
            if abs(nums[i] - 0)<inf:
                inf = abs(nums[i]-0)
                p = -1*(inf)
        if inf in nums:
            return inf
        else:
            return p


        