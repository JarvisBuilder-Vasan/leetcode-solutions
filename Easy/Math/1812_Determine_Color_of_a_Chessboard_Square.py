class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        total=0
        alpha=coordinates[0]
        num=int(coordinates[1])
        total=ord(alpha)-ord('a')+1
        total+=num
        
        if total%2==0:
            return False
        else:
            return True
