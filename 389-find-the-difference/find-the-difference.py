class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        m=""
        for i  in t:
            if i  in s:
                s=s.replace(i,"",1)
            else:
                m+=i
        return m       