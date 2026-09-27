class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        left=0
        mid=0
        right=n-1
        while mid<=right:
            if nums[mid]==0:
                temp=nums[left]
                nums[left]=nums[mid]
                nums[mid]=temp
                left+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                temp=nums[mid]
                nums[mid]=nums[right]
                nums[right]=temp
                right-=1
