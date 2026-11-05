class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        large = n - 1
        right = n -2
        combo = 0
        if len(nums) < 3:
            return 0

        while left != right:
            if nums[left] + nums[right] > nums[large]:
                combo += right - left
                right-=1
            else:
                left+=1
            
            if left == right:
                large -=1
                left = 0
                right = large - 1

        return combo
   
    