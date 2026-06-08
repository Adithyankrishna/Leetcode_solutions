class Solution:
    def hIndex(self, citations: List[int]) -> int:

        citations.sort()
        l = len(citations)
        for i in range(l):
            h = l - i
            if citations[i] >= h:
                return h
        return 0