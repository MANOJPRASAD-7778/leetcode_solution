class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        a=[]
        for i in nums:
            a.append(i)
        ans=[]
        ans=a+nums
        return ans



        