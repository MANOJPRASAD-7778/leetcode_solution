class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n=len(nums)
        low=0
        high=0
        su=0
        min_len=float("inf")
        if sum(nums)<target:
            return 0
        while(high<n):
            su+=nums[high]
            while(su>=target):
                min_len=min(min_len,(high-low)+1)
                su-=nums[low]
                low+=1
            high+=1
        return min_len    

        