class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum=0
        rsum=0
        mx=float("-inf")
    
        for i in range(k):
            lsum+=cardPoints[i]
        mx=max(mx,lsum)
        j=len(cardPoints)-1
        
        while(i>=0):
            lsum -=cardPoints[i]
            i-=1
            rsum+=cardPoints[j]
            j-=1
            mx=max(mx,(rsum+lsum))       
        return mx