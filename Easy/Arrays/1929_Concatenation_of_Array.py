class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        newsize = 2 * n
        ans = [0] * newsize

        for i in range(newsize):
            ans[i] = nums[i % n]

        return ans
