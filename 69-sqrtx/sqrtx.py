class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
            
        low = 0
        high = x
        while low <= high:
            mid = (low + high)//2
            sqr = mid*mid
            if sqr == x:
                return mid
            elif x > sqr:
                low =mid +1
            else:
                high = mid-1
           
        return high
                
        