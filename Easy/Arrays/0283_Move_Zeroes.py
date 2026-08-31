class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        right=0
        temp=0
        while right<=len(nums)-1:
            if nums[left]!=0 and nums[right]!=0:
                left+=1
                right+=1
                if left>len(nums)-1:
                    continue
            elif nums[left]==0 and nums[right]==0:
                right+=1
                continue
            if nums[left]==0 and nums[right]!=0:
                temp=nums[left]
                nums[left]=nums[right]
                nums[right]=temp
                left+=1
                right+=1
            
                
