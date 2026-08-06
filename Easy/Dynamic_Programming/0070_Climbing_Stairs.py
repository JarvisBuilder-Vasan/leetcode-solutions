class Solution:
    def climbStairs(self, n: int) -> int:
        first=0
        prev=0
        count=0
        for i in range(1,n+1):
            if i==1:
                first=i
                count+=1
            elif i==2:
                prev=i
                count+=1
            else:
                current=first+prev
                count=current
                first=prev
                prev=current
        return count
