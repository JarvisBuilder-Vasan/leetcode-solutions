class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        left=0
        right=0
        while left<len(name) and right<len(typed):
            if name[left]==typed[right]:
                right+=1
                left+=1
            elif right>0 and typed[right]==typed[right-1]:
                right+=1
            else:
                return False

        if left<len(name):
            return False

        while right<len(typed):
            if typed[right-1]==typed[right]:
                right+=1
            else:
                return False
        return True 
