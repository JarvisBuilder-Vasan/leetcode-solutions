class Solution:
    def countAsterisks(self, s: str) -> int:
        inside=False
        count=0
        for i in range(len(s)):
            if s[i]=='|':
                inside=not inside
            if s[i]=='*':
                if inside==False:
                    count+=1

        return count
