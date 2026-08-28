class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        rev=0
        temp=num
        while num>0:
            bal=num%10
            rev=(rev*10)+bal
            num=num//10
        old=0
        while rev>0:
            bal1=rev%10
            old=(old*10)+bal1
            rev=rev//10

        if old == temp:
            return True
        else:
            return False
