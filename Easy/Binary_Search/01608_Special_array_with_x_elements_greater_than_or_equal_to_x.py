class Solution:
    def specialArray(self, nums: list[int]) -> int:
        low=0
        high=len(nums)
        nums.sort()
        while left<=right:
            mid=low+(high-low)//2
            count=0
            for num in nums:
                if num>=mid:
                   count+=1
            if mid==count:
               return mid
            elif mid<count:
               low=mid+1
            else:
               high=mid-1
        return -1
           
