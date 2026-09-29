class Solution: 
    def minimumAverage(self, nums: List[int]) -> float: 
        nums.sort() 
        left=0 
        right=len(nums)-1 
        arr=[] 

        while left<=right: 
            mini=nums[left] 
            maxi=nums[right] 
            avg=(mini+maxi)/2 
            arr.append(avg) 
            left+=1 
            right-=1 
 
        return min(arr)
