class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        left=0
        right=len(nums)-1
        pos=0
        neg=0
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]>0:
                right=mid-1
            else:
                left=mid+1
        pos=len(nums)-left

        left=0
        right=len(nums)-1
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]>=0:
                right=mid-1
            else:
                left=mid+1
        neg=left
        if pos<neg:
            return neg
        else:
            return pos
