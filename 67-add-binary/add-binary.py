class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aa = int(a,2)
        bb = int(b,2)
        sum = aa + bb
        return bin(sum)[2:]

        