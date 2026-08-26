class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product=1
        for i in range(len(nums)):
            product*=nums[i]
        res=1
        if product>0:
            return res
        elif product==0:
            return res-1
        else:
            return -res
