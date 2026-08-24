class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res=0
        for i in range(len(nums)):
            count=0
            current=nums[i]
            while current>0:
                current=current//10
                count+=1
            if count%2==0:
                res+=1
        return res
