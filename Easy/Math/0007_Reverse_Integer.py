class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        temp=x
        x=abs(x)

        while x>0:
            rem=x%10
            rev=rev*10+rem
            x=x//10

        if rev > 2**31-1:
            return 0

        if temp<0:
            return -rev

        return rev
