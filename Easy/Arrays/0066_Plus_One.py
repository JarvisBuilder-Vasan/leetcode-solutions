class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        first = 0

        for i in range(len(digits)):
            first = first * 10 + digits[i]

        first += 1
        s = str(first)

        ans = []
        for ch in s:
            ans.append(int(ch))

        return ans
