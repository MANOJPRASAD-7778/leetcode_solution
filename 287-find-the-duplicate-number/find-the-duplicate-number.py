class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        fre={}
        for i in nums:
            if i in fre:
                fre[i]+=1
            else:
                fre[i]=1
        for keys,value in fre.items():
            if value>1:
                return keys            
        