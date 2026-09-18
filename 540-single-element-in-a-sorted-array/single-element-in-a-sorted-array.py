class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        fre={}
        for i in nums:
            if i in fre:
                fre[i]+=1
            else:
                fre[i]=1
        for keys,values in fre.items():
            if  values==1:
                return keys            
        