class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sSum = 0
        tSum = 0

        for i in range(len(s)):
            sSum ^= ord(s[i])

        for j in range(len(t)):
            tSum ^= ord(t[j])

        return chr(tSum ^ sSum)
