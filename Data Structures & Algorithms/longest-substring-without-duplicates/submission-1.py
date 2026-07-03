class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for i in range(len(s)):
    
            emptySet = set()
            
            for j in range(i,len(s)):

                if s[j] not in emptySet:
                    emptySet.add(s[j])
                else:
                    break
                longest = max(longest,len(emptySet))   
        
        return longest
                