class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum = 0
        rsum = 0
        mx = float("-inf")
        l = k - 1
        r = len(cardPoints) - 1
        for i in range(k):
            lsum += cardPoints[i]
        mx = max(mx, lsum)
        while l >= 0:
            lsum -= cardPoints[l]
            l -= 1
            rsum += cardPoints[r]
            r -= 1
            mx = max(mx, lsum + rsum)
        return mx