class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack=[]
        for ch in operations:
            if ch not in "+,D,C":
                stack.append(int(ch))
            else:
                if ch=='C':
                    stack.pop()
                if ch=="+":
                    stack.append(int(stack[-1])+int(stack[-2])) 
                if ch=="D":
                    stack.append(int(stack[-1])*2)    
        s=sum(stack) 
        return s           