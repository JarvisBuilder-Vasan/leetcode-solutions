class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen=nums[0]
        k=1
        for i in range(1,len(nums)):
            if seen==nums[i]:
                continue
            else:
                nums[k]=nums[i]
                k+=1
                seen=nums[i]

        return k
