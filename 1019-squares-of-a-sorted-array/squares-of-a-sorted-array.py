class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        postive=[]
        negative=[]
        for k in nums:
            if k<0:
                negative.append(k*k)
            else:
                postive.append(k*k)
        s_negative=negative[::-1]
        if len(postive)==0:
            return s_negative
        if len(s_negative)==0 :
            return postive   
        i=0
        j=0
        result=[]
        while(i<len(postive)and j<len(s_negative)):
            if postive[i]<s_negative[j] :
                result.append(postive[i])
                i+=1
            else:
                result.append(s_negative[j]) 
                j+=1
        while(i<len(postive)):
            result.append(postive[i]) 
            i+=1
        while(j<len(s_negative)) :
            result.append(s_negative[j]) 
            j+=1
        return result    



        