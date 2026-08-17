class Solution:
    def arrangeCoins(self, n: int) -> int:
        row=0
        count=0
        coins=1
        while(row<n):
            row=coins
            n-=row
            coins+=1
            count+=1

        return count
