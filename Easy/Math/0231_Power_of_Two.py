class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return True
        while n>0:
            bal=n%2
            n=n//2
            if n==1 and bal==0:
                return True
            elif bal==1:
                break
            
        return False
