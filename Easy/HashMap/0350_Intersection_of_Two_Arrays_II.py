class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic={}

        for num in nums1:
            if num in dic:
                dic[num]+=1
            else:
                dic[num]=1
            
        ans=[]
        count=0
        for i in range(len(nums2)):
            if nums2[i] in dic and dic[nums2[i]]>0:
                ans.append(nums2[i])
                dic[nums2[i]]-=1

        return ans
