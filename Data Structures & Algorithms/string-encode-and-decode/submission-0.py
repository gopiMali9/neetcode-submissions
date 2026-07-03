class Solution:

    def encode(self, strs: List[str]) -> str:

        random_num  = 424
        output = []
        for i in str(strs):
            output.append(str(ord(i)+424))
        
        return "+".join(output)

            

    def decode(self, s: str) -> List[str]:

        print(s)

        output = ''

        for j in s.split('+'):
            num =int(j)-424
            output += str(chr(num))
        
        return eval(output)


