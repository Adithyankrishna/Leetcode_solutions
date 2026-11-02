class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # index = -1
        # start = 0
        # while start != len(haystack):
        #     if needle[i] == haystack[start]:
        #         index = i
        #         i+=1
        #         start+=1
        #     else:
        #         start+=1
        #         i = 0
        # minindex = 0
        # start = 0

        # for i in range(len(haystack)):
        #     if needle[start] == haystack[i]:
        #         start+=1
        #         index = start
        #         minindex = min(minindex,index)
        #         if start ==len(needle):
        #             start = 0
        # return minindex


        k = len(needle)
        
        
        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:(i+k)] == needle:
                return i
        return -1
            