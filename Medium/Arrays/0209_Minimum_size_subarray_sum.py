class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        total=0
        mini=float('inf')
        left=0
        for i in range(len(nums)):
            total+=nums[i]
            while total>=target:
                mini=min(mini,abs(i-left+1))
                total-=nums[left]
                left+=1
                
        if mini!=float('inf'):
            return mini
        else:
            return 0
