class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        double_total=0
        single_total=0
        for i in nums:
            if i>9:
                double_total+=i
            else:
                single_total+=i    
        alice=max(double_total,single_total)   
        bob=(double_total+single_total)-alice    
        if alice>bob:
            return True
        else:
            return False    
              