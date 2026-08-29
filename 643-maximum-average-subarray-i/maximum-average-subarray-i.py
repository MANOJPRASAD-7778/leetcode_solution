class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        su=0
        r=0
        l=0
        mx_sum=float("-inf")
        while(r<k):
            su+=nums[r]
            r+=1
        mx_sum=max(mx_sum,su)
        while(r<len(nums)):
            su-=nums[l]
            l+=1
            su+=nums[r]
            r+=1

            mx_sum=max(mx_sum,su)
        return (mx_sum)/k





        