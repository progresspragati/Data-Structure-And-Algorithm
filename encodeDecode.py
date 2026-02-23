from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = ""
        for str in strs:
            for ch in str:
                encode_str += chr(ord(ch)+4)
            encode_str += "£"
        return encode_str

    def decode(self, s: str) -> List[str]:
        strs = []
        word = ""
        for ch in s:
            if ch == "£":
                strs.append(word)
                word = ""
            else:
                word += chr(ord(ch)-4)
        return strs
    
    def encodeOptimal(self, strs: List[str]) -> str:
        encode_string = ""
        for word in strs:
            encode_string += str(len(word)) + "#" + word
        return encode_string

    def decodeOptimal(self, s: str) -> List[str]:
        decode_list = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length 
            decode_list.append(s[i:j])
            i = j
        return decode_list
            
    
    
result = Solution()
print(result.encodeOptimal(["The quick brown fox","jumps over the","lazy dog","1234567890","abcdefghijklmnopqrstuvwxyz"]))
print(result.decodeOptimal(result.encodeOptimal(["The quick brown fox","jumps over the","lazy dog","1234567890","abcdefghijklmnopqrstuvwxyz"])))

