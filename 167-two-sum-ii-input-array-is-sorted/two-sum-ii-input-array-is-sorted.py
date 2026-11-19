class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        while(i<j):
            s=0
            s=numbers[i]+numbers[j]
            if s==target:
                break
            if s>target:
                j-=1
            if s<target:
                i+=1   
        return[i+1,j+1]       

        