from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: list[int]) -> str:

        arr = list(map(str, nums))

        def compare(a, b):
            if a + b > b + a:
                return -1
            if b + a > a + b:
                return 1
            return 0

        arr.sort(key=cmp_to_key(compare))

        if arr[0] == "0":
            return "0"

        return "".join(arr)