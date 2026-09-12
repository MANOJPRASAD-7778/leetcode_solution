class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        count = 0
        su = 1
        l = 0

        for r in range(len(nums)):
            su *= nums[r]

            while su >= k:
                su //= nums[l]
                l += 1

            count += r - l + 1

        return count