class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        mini=0
        cap=float('inf')
        ind=-1
        for i in range(len(capacity)):
            if capacity[i]>=itemSize:
                mini=capacity[i]-itemSize
                if mini<cap:
                    cap=mini
                    ind=i
        return ind
