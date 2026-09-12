class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0:
            return "0"
        ans=0
        place=1
        neg=num<0
        if neg:
            num=-num
        while num>0:
            rem=num%7
            num=num//7
            ans+=rem*place
            place*=10
        if neg:
            ans=-ans
        return str(ans)
