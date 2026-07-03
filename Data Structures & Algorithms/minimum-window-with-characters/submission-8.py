class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ''
        elif t == s:
            return t

        output = []

        for i in range(len(s)):

            if s[i] in t:
                left = i
                eq = list(t)
                count = 0

                while eq:
                    
                    if left == len(s):
                        break

                    if s[left] in eq:
                        eq.remove(s[left])
                    
                    left += 1
                    count += 1

                if len(eq) == 0:
                    output.append(s[i:i+count])
        st = sorted(output,key=len)
        print(st)

        if len(st) == 0:
            return ''
        else:
            return st[0]
        


        
        