class Solution:

    def findGCD(self, nums: List[int]) -> int:

        mini = nums[0]
        maxi = nums[0]

        for i in range(len(nums)):
            if nums[i] < mini:
                mini = nums[i]

            if nums[i] > maxi:
                maxi = nums[i]

        gcd = 1

        for i in range(1, mini + 1):
            if mini % i == 0 and maxi % i == 0:
                gcd = i

        return gcd
