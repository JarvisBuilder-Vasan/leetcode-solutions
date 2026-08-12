class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[0]*n
        left=0
        right=n-1
        pos=n-1
        for i in range(n):
            if abs(nums[left])<abs(nums[right]):
                current=nums[right]**2
                result[pos]=current
                right-=1
            else:
                current=nums[left]**2
                result[pos]=current
                left+=1
            pos-=1
        return result
