class Solution:
    def addDigits(self, num: int) -> int:
        bal = 0
        total = 0

        while num >= 10:
            total = 0

            while num > 0:
                bal = num % 10
                total += bal
                num = num // 10

            num = total

        return num
