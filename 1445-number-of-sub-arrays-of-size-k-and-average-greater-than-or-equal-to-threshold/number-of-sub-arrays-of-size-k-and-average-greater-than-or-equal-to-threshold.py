class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l=0
        r=k-1
        s=0
        c=0
        for i in range(r+1):
            s+=arr[i]
        if s/k>=threshold:
            c+=1
        while(r<len(arr)-1):
            s-=arr[l]
            r+=1
            s+=arr[r]
            l+=1
            if((s//k)>=threshold):
                c+=1
        return c        
        