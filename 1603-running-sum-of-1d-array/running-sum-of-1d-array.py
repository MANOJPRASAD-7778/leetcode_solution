class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a=[]
        su=0
        for i in range(0,len(nums)):

            su=su+nums[i]
            a.append(su)
        return a    

        