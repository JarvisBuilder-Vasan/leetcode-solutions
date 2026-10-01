class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        sum_=-1
        ans=[]

        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1

            while(l<r):
                sum_=nums[i]+nums[l]+nums[r]
                triplets=[nums[i],nums[l],nums[r]]

                if sum_==0:
                    ans.append(triplets)
                    l+=1
                    r-=1

                    while(l<r and nums[l]==nums[l-1]):
                        l+=1
                    
                    while(l<r and nums[r]==nums[r+1]):
                        r-=1

                elif sum_<0:
                    l+=1

                else:
                    r-=1

        return ans
