class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        output = []
        for i in range(len(strs)):
            match = []
            temp = strs[:i]+strs[i+1:]
            match.append(strs[i])
            for j in temp:
                if sorted(strs[i]) == sorted(j):
                    match.append(j)
            if sorted(match) not in [sorted(z) for z in output]:
                output.append(match)
        
        return output


        