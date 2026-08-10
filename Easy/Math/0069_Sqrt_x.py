class Solution:
    def mySqrt(self, x: int) -> int:
        l=1
        r=x

        while(l<=r):
            m=l+(r-l)//2
            sq=m**2

            if x==sq:
                return m
            elif sq<x:
                l=m+1
            else:
                r=m-1
        return r
