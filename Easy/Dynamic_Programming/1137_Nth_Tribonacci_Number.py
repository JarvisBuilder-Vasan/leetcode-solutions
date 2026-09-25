class Solution:
    def tribonacci(self, n: int) -> int:
        sum=0
        a=0
        b=1
        c=1

        if n==0:
            return 0
        for i in range(c+1,n):
            sum=a+b+c 
            a=b
            b=c
            c=sum

        return c
