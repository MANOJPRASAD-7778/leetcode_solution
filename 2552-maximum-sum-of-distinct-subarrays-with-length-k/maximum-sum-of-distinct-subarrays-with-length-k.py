class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        s = 0
        m = 0
        st = set()
        while r < len(nums):

            while nums[r] in st:
                st.remove(nums[l])
                s -= nums[l]
                l += 1

            st.add(nums[r])
            s += nums[r]

            if r - l + 1 == k:
                m = max(m, s)
                st.remove(nums[l])
                s -= nums[l]
                l += 1
            r += 1

        return m
        