class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        left=0
        right=1
        while left<len(nums) and right<len(nums):
            if nums[left]%2==0:
                left+=2
            elif nums[right]%2!=0:
                right+=2
            else:
                temp=nums[left]
                nums[left]=nums[right]
                nums[right]=temp
                left+=2
                right+=2
        return nums
