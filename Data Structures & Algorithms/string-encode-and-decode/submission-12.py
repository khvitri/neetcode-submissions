DELIMITER = "?"

class Solution:

    def encode(self, strs: List[str]) -> str:
        # ["Hello", "World"] -> "5?Hello5?World"
        strsEncoded = ""
        for s in strs:
            strsEncoded += str(len(s)) + DELIMITER + s            
        
        return strsEncoded

    def decode(self, s: str) -> List[str]:
        sDecoded = []
        i = j = 0
        while i < len(s):
            while s[j] != DELIMITER:
                j += 1
            count = int(s[i:j])
            sDecoded.append(s[j + 1:j + count + 1])
            i = j = j + count + 1
        
        return sDecoded
            
            
