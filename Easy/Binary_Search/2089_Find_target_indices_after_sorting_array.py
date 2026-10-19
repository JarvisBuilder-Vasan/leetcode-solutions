class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
      first=-1
      res=[]
      left=0
      right=len(nums-1)
      nums.sort()
      while left<=right:
        mid=left+(right-left)//2
        if nums[mid]==target:
          first=mid
          right=mid-1
        elif nums[mid]<target:
          left=mid+1
        else:
          right=mid-1
      i=first
      while i<len(nums) and nums[i]==target:
        res.append(i)
        i+=1
      return res
