# LeetCode 35 - Search Insert Position
# Difficulty: Easy
# Approach: Linear Search
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.sort()
        l=0
        r=len(nums)-1

        while(l<=r):
            mid=(r+l)//2

            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1

        if nums[mid]!=target:
            return l
