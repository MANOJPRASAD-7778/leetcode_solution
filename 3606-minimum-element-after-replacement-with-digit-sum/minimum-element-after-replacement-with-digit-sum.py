class Solution:
    def minElement(self, nums: List[int]) -> int:
        r=[]
        for i in range(len(nums)):
            su=0
            temp=nums[i]
            while(temp>0):
                re=temp%10
                su+=re
                temp=temp//10
            r.append(su) 
        return min(r)      

        