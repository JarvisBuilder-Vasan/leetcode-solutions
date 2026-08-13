class Solution:
    def romanToInt(self, s: str) -> int:
        dic={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        right=1
        total=0
        n=len(s)
        for i in range(n):
            current=dic[s[i]]
            if right<=n-1 and current>=dic[s[right]]:
                total+=current
                right+=1
            elif right>n-1:
                total+=current
            else:
                total-=current
                right+=1
        return total
