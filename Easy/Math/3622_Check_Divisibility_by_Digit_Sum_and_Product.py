class Solution:
    def checkDivisibility(self, n: int) -> bool:
        n = str(n)
        total = 0
        product = 1

        for i in range(len(n)):
            total += int(n[i])
            product *= int(n[i])

        overall = total + product
        n = int(n)

        if n % overall == 0:
            return True
        else:
            return False
