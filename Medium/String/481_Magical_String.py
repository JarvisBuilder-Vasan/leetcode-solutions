class Solution:

    def magicalString(self, n: int) -> int:

        s = "122"
        left = 2
        current = "1"

        while len(s) < n:

            if s[left] == "1":
                s += current
            else:
                s += current
                s += current

            left += 1

            if current == "1":
                current = "2"
            else:
                current = "1"

        count = 0

        for i in range(n):
            if s[i] == "1":
                count += 1

        return count
