class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        fre={}
        for i in nums:
            if i in fre:
                fre[i]+=1
            else:
                fre[i]=1
        for key, value in fre.items():
            if value==1:
                return key

        