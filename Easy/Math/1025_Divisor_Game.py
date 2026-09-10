class Solution:
    def divisorGame(self, n: int) -> bool:
        x=1
        alice=False
        while x<n:
            if n%x==0:
                alice=not alice
            n-=x
        return alice
