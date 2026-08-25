class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result=[]
        while left<=right:
            current=left
            number=current
            is_correct=True
            while current>0:
                digits=current%10
                if digits==0:
                    is_correct=False
                    break
                if number%digits!=0:
                    is_correct=False
                    break
                current=current//10
            if is_correct:
                result.append(left)
            left+=1
            
        return result
