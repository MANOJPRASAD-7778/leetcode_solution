class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m=0

        for i in accounts:
            s=0
            s=sum(i)
            m=max(m,s)
        return m    

        