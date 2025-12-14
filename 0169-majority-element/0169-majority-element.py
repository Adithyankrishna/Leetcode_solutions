class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = 0
        for i in range(len(nums)):
            current = i
            if count == 0:
                candidate = nums[current]
            if candidate ==nums[current]:
                count+=1
            else:
                count-=1
        return candidate