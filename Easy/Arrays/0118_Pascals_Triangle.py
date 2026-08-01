class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            rows = [1] * (i + 1)
            if i > 1:
                previous = ans[i - 1]
                for j in range(1, i):
                    rows[j] = previous[j - 1] + previous[j]
            ans.append(rows)
        return ans
