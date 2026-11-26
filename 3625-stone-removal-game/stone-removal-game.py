class Solution:
    def canAliceWin(self, n: int) -> bool:
        x=10
        if n<=9:
            return False
        while(n>=0):
            if (n-x)>=0:
                n=n-x
                x-=1
            else:
                return False
            if (n-x)>=0:
                n=n-x
                x-=1
            else:
                return True

        