class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        current=0
        total=0
        for i in range(len(requests)):
            total+=abs(current-requests[i])
            current=requests[i]

        return total
