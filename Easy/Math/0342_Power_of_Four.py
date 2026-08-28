class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return True

        while n>0:
            bal=n%4
            n=n//4

            if n==1 and bal==0:
                return True
            elif bal>=1:
                return False

        return False
