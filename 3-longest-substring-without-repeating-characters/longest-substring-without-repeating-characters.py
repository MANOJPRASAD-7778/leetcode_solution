class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        mx=0
        for i in range(len(s)):
            count=0
            seen=set()
            for j in range(i,len(s)):
                if s[j] in seen:
                    break
                else:
                    seen.add(s[j])
                    count+=1
                    mx=max(mx,count)
        return mx            
        