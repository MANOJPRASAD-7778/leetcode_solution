class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        r=[]
        s=[]
        for i in range(1,n+1):
            if i%m==0:
                r.append(i)
            else:
                s.append(i)    
        return (sum(s)-sum(r))        
        