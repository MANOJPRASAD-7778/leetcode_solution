class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        r=[]
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1   
        for value in d.values():
            r.append(value)
        m=set(r)    
        if len(r)== len(m):
            return True
        else:
            return False               
                 
        