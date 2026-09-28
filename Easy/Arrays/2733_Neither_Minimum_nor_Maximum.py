class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums)>2:
            maxi=max(nums)
            nums.remove(maxi)
            mini=min(nums)
            nums.remove(mini)
            return nums[0]
        else:
            return -1
