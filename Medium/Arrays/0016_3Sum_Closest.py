class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        csum=-1
        nums.sort()
        best_diff=float('inf')
        
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1

            while(l<r):
                csum=nums[i]+nums[l]+nums[r]
                current_diff=abs(target-csum)

                if current_diff<best_diff:
                    best_diff=current_diff
                    close_target=csum
                if csum==target:
                    return csum
                elif csum<target:
                    l+=1
                else:
                    r-=1

        return close_target
