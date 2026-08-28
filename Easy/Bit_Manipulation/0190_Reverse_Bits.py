class Solution:
    def reverseBits(self, n: int) -> int:
        result=0
        bits=32

        for i in range(bits):
            result=(result << 1) | (n&1)
            n>>=1

        return result
