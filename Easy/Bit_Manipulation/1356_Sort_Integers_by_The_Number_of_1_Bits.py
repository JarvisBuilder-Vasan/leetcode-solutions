class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        result=[]
        for i in range(len(arr)):
            count=0
            n=arr[i]
            while n>0:
                bit=n&1
                if bit==1:
                    count+=1
                n>>=1
            tup=(count,arr[i])
            result.append((count,arr[i]))
        result.sort()

        answer=[0]*len(result) 
        for i in range(len(result)):
            answer[i]=result[i][1]

        return answer

                
            

            

            
