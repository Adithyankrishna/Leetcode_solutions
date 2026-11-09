class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        seen = {}

        for i , char in enumerate(s):
            seen[char] = i
        

        end = 0
        res = []
        prev = 0

        for i in range(len(s)):
            end = max(end , seen[s[i]])
            if i == end:

                res.append((i+1)- prev)
                prev = i+1
        return res

    