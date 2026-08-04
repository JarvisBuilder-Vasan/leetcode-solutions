class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for char in s:
            if char.isalnum():
                new += char

        new = new.lower()
        rev = new[::-1]

        if rev == new:
            return True
        else:
            return False
