class Solution:

    def distinctAverages(self, nums: list[int]) -> int:
        nums.sort()

        left = 0
        right = len(nums) - 1
        empty_set = set()

        while left <= right:
            mini = nums[left]
            maxi = nums[right]
            avg = (mini + maxi) / 2
            empty_set.add(avg)

            left += 1
            right -= 1

        return len(empty_set)
