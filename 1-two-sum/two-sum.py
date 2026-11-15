class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        r=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    r.append(i)
                    r.append(j)
                    break
            
        return r                   