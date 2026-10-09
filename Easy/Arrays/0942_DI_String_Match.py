class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        left=0
        right=len(s)
        arr=[]
        i=0
        while i<len(s):
            if s[i]=="I":
                arr.append(left)
                left+=1
            elif s[i]=="D":
                arr.append(right)
                right-=1
            i+=1
        arr.append(left)
        return arr
