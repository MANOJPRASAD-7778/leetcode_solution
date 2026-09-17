class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        fre={}
        r=[]
        for i in  nums:
            if i in fre:
                fre[i]+=1
            else:
                fre[i]=1
        for keys ,value in fre.items():
            if value==2:
                r.append(keys) 
        return r                   
        