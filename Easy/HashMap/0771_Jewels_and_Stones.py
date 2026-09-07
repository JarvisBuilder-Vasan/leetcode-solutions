class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dic={}
        for i in range(len(jewels)):
            if jewels[i] in dic:
                dic[jewels[i]]+=1
            else:
                dic[jewels[i]]=1
        count=0
        for j in range(len(stones)):
            if stones[j] in dic:
                count+=1
        return count
