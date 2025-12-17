from typing import List
class Solution:
    def encode(self, strs: List[str]) -> str:
        str = ""
        i = 0
        while i < len(strs):
            for x in strs[i]:
                str = str + chr(ord(x)+ 4)
            str = str + " "
            i += 1 
        return str   

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        str1 = ""
        for x in str:
            if(x != " "):
                str1 = str1 + chr(ord(x) -4)
            else:
                strs.append[str1]
                str1 = ""
        return strs
    
result = Solution()
print(result.decode())

            
