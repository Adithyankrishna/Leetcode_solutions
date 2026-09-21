class Solution:
    def compress(self, chars: list[str]) -> int:

        count = 1
        result = ""
        left = 0
        right = 1

        while right != len(chars):
            if chars[left] == chars[right]:
                count +=1
                left+=1
                right+=1
            else:
                result +=chars[left]
                if count > 1:
                    result += str(count)
                left+=1
                right+=1
                count = 1
        result += chars[left]
        if count > 1:
            result +=str(count)
        chars[:] = list(result)
        return len(result)












        # for i in range(len(chars)-1):
        #     if chars[i] == chars[i+1]:
        #         count +=1
        #     else:
        #         result += chars[i]
        #         result += str(count)
        #         count = 1
        # return len(result)
            
        