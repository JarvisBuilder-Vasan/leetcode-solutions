class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
      lis=[]
      for i in range(len(nums)):
        index=abs(nums[i])-1
        if nums[index]<0:
          lis.append(abs(nums[i])
        else:
          nums[index]=-nums[index]
      return lis
