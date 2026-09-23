class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False

        div = 1
        total = 0

        while div <= num**0.5:
            if num % div == 0:
                total += div

                if div != 1 and div != num // div:
                    total += num // div

            div += 1

        if total == num:
            return True
        else:
            return False
