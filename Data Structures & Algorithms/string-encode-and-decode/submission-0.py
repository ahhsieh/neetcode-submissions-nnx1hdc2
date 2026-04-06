import json

class Solution:

    def encode(self, strs: List[str]) -> str:
        builder = []
        for s in strs:
            length_code = chr(ord("\n") + len(s))
            builder.append(length_code)
            builder.append(s)
        return "".join(builder)

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            length_code = s[i]
            length = ord(length_code) - ord("\n")
            strs.append(s[i+1:i+length+1])
            i = i + length + 1
        return strs
