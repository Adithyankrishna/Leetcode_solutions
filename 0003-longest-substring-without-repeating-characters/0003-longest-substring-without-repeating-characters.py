class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = []
        maxlen = 0
        for char in s:
            if char in arr:
                while char in arr:
                    arr.pop(0)
            arr.append(char)
            maxlen = max(maxlen,len(arr))
        return maxlen