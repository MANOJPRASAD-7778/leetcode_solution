class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.append(target)
        l=list(set(nums))
        l.sort()
        return l.index(target)
        
        