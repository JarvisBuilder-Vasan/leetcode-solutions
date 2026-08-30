class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        
        while(n>0):
            if n&1==1:
                count+=1
                new=n>>1
                n=new       
            else:
                new=n>>1
                n=new 
        
        return count

        if n==0:
            return 0
        
