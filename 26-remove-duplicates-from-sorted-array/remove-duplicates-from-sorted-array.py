class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        officer=0
        cm=1
        result=1
        while(cm<len(nums)):
            if nums[cm]==nums[cm-1]:
                cm+=1
            else:
                nums[officer+1]=nums[cm]
                cm+=1
                result+=1
                officer+=1
        return result        



        