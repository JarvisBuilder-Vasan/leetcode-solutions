class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        n=len(letters)
        new_Str=""
        while columnNumber>0:
            bal=columnNumber%n
            div=columnNumber//n
            if bal!=0:
                new_Str+=letters[bal-1]
                columnNumber=div
            else:
                new_Str+=letters[-1]
                columnNumber=div-1
            if div!=0:
                continue
            else:
                break

        return new_Str[::-1]
