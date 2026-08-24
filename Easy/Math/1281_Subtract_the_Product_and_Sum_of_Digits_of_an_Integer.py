class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        total=0
        product=1
        while n>0:
            bal=n%10
            n=n//10
            total+=bal
            product*=bal

        res=product-total
        return res
