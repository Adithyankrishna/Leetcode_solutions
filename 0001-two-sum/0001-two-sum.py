class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i , num in enumerate(nums):
            k = target - num
            if k in seen:
                return(seen[k],i)
            seen[num] =i
        