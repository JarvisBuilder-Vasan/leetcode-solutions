class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candy={}
        diet=len(candyType)//2
        count=0
        for i in range(len(candyType)):
            if count<diet:
                if candyType[i] in candy:
                    continue
                else:
                    candy[candyType[i]]=1
                    count+=1
            else:
                break
            
        return count
