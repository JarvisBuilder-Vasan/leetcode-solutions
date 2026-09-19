class Solution:
    def isHappy(self, n: int) -> bool:
        sum_=0
        ind=0
        seen=set()
        while(n!=1):
            if n in seen:
                return False
            seen.add(n)
            sum_=0
            while(n>0):
                ind=n%10    
                n=n//10
                ind*=ind
                sum_=sum_+ind
            n=sum_
        return True
