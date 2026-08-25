class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        dis=0
        min_dis=float('inf')
        ans=-1
        for i in range(len(drones)):
            x=drones[i][0]
            y=drones[i][1]
            rang=drones[i][2]
            dis=abs(x-target[0])+abs(y-target[1])
            if dis<=rang:
                if dis<min_dis:
                    min_dis=dis
                    ans=i

        return ans
                
            
