class Solution:
    def calPoints(self, operations: List[str]) -> int:
        rec=[]
        first=0
        previous=0
        for i in range(len(operations)):
            current=operations[i]
            first=previous-1
            if current=="C":
                del rec[previous]
                previous-=1
            elif current=="D":
                double=rec[previous]*2
                rec.append(double)
                previous=len(rec)-1
            elif current=="+":
                plus=int(rec[first])+int(rec[previous])
                rec.append(plus)
                previous=len(rec)-1
            else:
                rec.append(int(operations[i]))
                previous=len(rec)-1
        return sum(rec)
