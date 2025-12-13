class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxlen = 0
        for num in seen:
            if num-1 not in seen:
                currnum = num
                currlen = 1
                while currnum+1 in seen:
                    currnum = currnum + 1
                    currlen +=1
                if currlen > maxlen:
                    maxlen = currlen
        return maxlen

        