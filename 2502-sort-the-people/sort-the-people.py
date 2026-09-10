class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        r=[]
        r=heights.copy()
        r.sort(reverse=True)
        ans=[]
        for i in r:
            ans.append(names[heights.index(i)])
        return ans    


    