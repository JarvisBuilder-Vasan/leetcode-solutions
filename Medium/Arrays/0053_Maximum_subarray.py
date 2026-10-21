class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
      currentsum=0
      maxisum=float('-inf')
      for i in range(len(nums)):
          currentsum+=nums[i]
          maxisum=max(currentsum,maxisum)
          if currentsum<0:
              currentsum=0
      return maxisum
