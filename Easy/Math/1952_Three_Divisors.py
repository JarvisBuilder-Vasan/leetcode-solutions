class Solution:
    def isThree(self, n: int) -> bool:
        if n==1:
            return False
        product=1
        perfect_square=False
        while product*product<=n:
            if product*product==n:
                perfect_square=True
                break
            product+=1

        if not perfect_square:
            return False

        for i in range(2,product):
            if product%i==0:
                return False

        return True
