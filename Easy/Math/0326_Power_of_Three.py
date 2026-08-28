class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==1:
            return True

        while n>0:
            bal=n%3
            n=n//3

            if n==1 and bal==0:
                return True
            elif bal>=1:
                return False

        return False
