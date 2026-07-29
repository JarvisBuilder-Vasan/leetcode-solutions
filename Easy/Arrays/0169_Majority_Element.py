class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic={}
        n=len(nums)//2
        for num in nums:
            if num in dic:
                dic[num]+=1
            else:
                dic[num]=1
        
        for i in range(len(nums)):
            if dic[nums[i]]>n:
                return nums[i]
