class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # output = False
        for i in range(len(s2)):
            if s2[i] in s1:
                right = i
                eq = list(s1)
                while eq:
                    if right == len(s2):
                        break
                    if s2[right] in s1 and s2[right] in eq:
                        eq.remove(s2[right])
                        right += 1
                    else:
                        break   
                if eq:
                    continue
                else:
                    return True
        return False
                    
