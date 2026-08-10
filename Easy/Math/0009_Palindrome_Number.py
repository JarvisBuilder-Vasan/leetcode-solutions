class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=x
        r=0
        while(x>0):
            d=x%10
            r=r*10+d
            x=x//10

        return n==r
