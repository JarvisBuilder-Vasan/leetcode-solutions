class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums.sort()
        empty_set=set()
        for i in range(len(nums)):
            empty_set.add(nums[i])

        empty_set=list(empty_set)
        empty_set.sort()

        if len(empty_set)>=3:
            if len(empty_set)==3:
                return (empty_set[0])
            else:
                ind=len(empty_set)-3
                return (empty_set[ind])
        else:
            return max(empty_set)
