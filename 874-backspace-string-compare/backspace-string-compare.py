class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1=[]
        for ch in s:
            if ch=="#":
                if stack1:
                    stack1.pop()
            else:
                stack1.append(ch)
        stack2=[]        
        for ch1 in t:
            if ch1=="#":
                if stack2:
                    stack2.pop()
            else:
                stack2.append(ch1)  
        return stack1 == stack2



        