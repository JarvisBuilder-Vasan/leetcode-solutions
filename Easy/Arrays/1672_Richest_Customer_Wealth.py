class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        total = 0
        great = 0

        for i in range(len(accounts)):
            total = 0
            for j in range(len(accounts[i])):
                total += accounts[i][j]

            if total > great:
                great = total

        return great
