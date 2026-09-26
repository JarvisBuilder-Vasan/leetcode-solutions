class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        dic = {}
        dic2 = {}
        diff = {}
        count = 0

        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]] += 1
                prev = dic2[nums[i]]
                currentdiff = i - prev

                if nums[i] in diff:
                    diff[nums[i]].append(currentdiff)
                else:
                    diff[nums[i]] = [currentdiff]

                dic2[nums[i]] = i
            else:
                dic[nums[i]] = 1
                dic2[nums[i]] = i

        for x in dic:
            if dic[x] == 3:
                if diff[x][0] == diff[x][1]:
                    count += 1

        return count
