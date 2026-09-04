class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i=1
        if n==1:
            return True
        while(2**i<=n):
            if 2**i==n:
                return True
            i+=1
        return False    


        