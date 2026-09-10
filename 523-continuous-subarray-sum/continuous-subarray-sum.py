class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        h_map={0:-1}
        pre=0
        for i,num  in enumerate(nums):
            pre+=num
            rem=pre%k
            if rem in h_map:
                if (i- h_map[rem])>=2:
                    return True
            else:
                h_map[rem]=i
        return False                