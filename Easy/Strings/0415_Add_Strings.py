class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i=len(num1)-1
        j=len(num2)-1
        total=0
        carry=0
        result=""

        while(i>=0 or j>=0 or carry):
                if i>=0:
                    d1=int(num1[i])
                else:
                    d1=0
                if j>=0:
                    d2=int(num2[j])
                else:
                    d2=0

                total=d1+d2+carry
                carry=total//10
                total=total%10

                result=str(total)+result

                i -= 1
                j -= 1

        return result
        
