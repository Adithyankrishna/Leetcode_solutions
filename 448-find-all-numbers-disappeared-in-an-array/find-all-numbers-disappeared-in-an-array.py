class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = []
        seen = set(nums)
        while n!=0:
            if n not in seen:
                result.append(n)
            n-=1
        return result
            

        