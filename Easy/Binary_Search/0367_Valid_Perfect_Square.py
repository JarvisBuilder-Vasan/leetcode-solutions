class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left=1
        right=num
        while(left<=right):
            mid=left+(right-left)//2
            sqr=mid**2

            if sqr==num:
                return True
            elif sqr<num:
                left=mid+1
            else:
                right=mid-1

        return False
