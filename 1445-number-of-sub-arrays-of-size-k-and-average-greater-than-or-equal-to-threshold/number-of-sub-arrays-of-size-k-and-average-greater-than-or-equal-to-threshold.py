class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l=0
        r=0
        su=0
        count=0
        while(r<k):
            su+=arr[r]
            r+=1
        if su/k>= threshold:
            count+=1
        while(r<len(arr)):
            su-=arr[l]
            l+=1
            su+=arr[r]
            r+=1
            if su/k >= threshold:
                count+=1 
        return count              