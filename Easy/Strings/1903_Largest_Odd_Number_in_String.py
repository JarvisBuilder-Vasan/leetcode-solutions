class Solution:
    def largestOddNumber(self, num: str) -> str:
        large=0
        for i in range(len(num)-1,-1,-1):
            last=num[-1]
            last=int(last)
            
            first=num[i]
            first=int(first)
            
            if last%2!=0:
                return num

            if first%2==0:
                continue
            else:
                return num[:i+1]
            
        return ""
