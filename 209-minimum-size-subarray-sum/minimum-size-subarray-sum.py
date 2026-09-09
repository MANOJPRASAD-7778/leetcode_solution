class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        k=target
        r=0
        mx=float("inf")
        su=0
        while(r<len(nums)):
            su+=nums[r] 
            while su>=k:
                mx=min(mx,r-l+1)
                su-=nums[l]
                l+=1
            r+=1  
        if mx==float("inf"):
            return 0     
        return mx