class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n<10:
            return False
        if 10<=n<=18:
            return True
        if 19<=n<27:
            return False
        if 27<=n<34:
            return True  
        if 34<=n<40:
            return False
        if 40<=n<45:
            return True
        if 45<=n<49:
            return False
        else:
            return True            

        
                
        