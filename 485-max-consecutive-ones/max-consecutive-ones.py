class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        su=0
        m=0
        for i in range(len(nums)):
            if nums[i]== 0:
                su=0
            else:
                su+=nums[i]
            m=max(m,su)
        return m    


        