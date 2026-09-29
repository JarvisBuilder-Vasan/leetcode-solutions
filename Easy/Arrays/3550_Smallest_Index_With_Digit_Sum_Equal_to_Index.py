class Solution:

    def smallestIndex(self, nums: List[int]) -> int:

        for i in range(len(nums)):

            total = 0

            while nums[i] > 9:
                total += nums[i] % 10
                nums[i] //= 10

            total += nums[i]

            if i == total:
                return i

        return -1
