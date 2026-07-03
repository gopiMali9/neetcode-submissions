class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maxL = 0

        for i in range(len(s)):
            check = set()
            for j in range(i,len(s)):
                if s[j] not in check:
                    check.add(s[j])
                    maxL = max(len(check),maxL)
                else:
                    break

        return maxL
        