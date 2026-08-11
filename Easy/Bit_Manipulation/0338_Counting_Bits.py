class Solution:
    def countBits(self, n: int) -> List[int]:
        result=[]
        count=0
        for i in range(n+1):
            count=0
            num=i
            while num!=0:
                new=num&1
                num=num>>1
                if new>=1:
                    count+=1
            result.append(count)
        return result
