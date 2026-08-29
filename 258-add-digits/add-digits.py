class Solution:
    def addDigits(self, num: int) -> int:
        def demo(num):
            f=num%10
            r=num//10
            return f+r
        while(num>9):
            num=demo(num)    
        return num    