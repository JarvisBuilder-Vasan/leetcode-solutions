class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic={}
        last=[]
        for num in nums1:
            if num in dic:
                dic[num]+=1
            else:
                dic[num]=1
            
        for i in range(len(nums2)):
            if nums2[i] not in last and nums2[i] in dic:
                last.append(nums2[i])

        return last
