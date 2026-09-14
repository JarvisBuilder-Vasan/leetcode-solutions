class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic1={}
        for i in range(len(list1)):
            dic1[list1[i]]=i
        min_index=float('inf')
        res=[]
        for j in range(len(list2)):
            if list2[j] in dic1:
                current_index=dic1[list2[j]]+j
                if current_index<min_index:
                    min_index=current_index
                    res=[]
                    res.append(list2[j])
                elif min_index==current_index:
                    res.append(list2[j])
        return res        
        
        
