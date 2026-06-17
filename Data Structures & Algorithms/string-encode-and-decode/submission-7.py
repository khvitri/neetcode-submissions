class Solution:

    """
    @param: s: the string to produce the length meta data for
    @return: the length metadata of the string
    """
    def _metaLen(self, s: str) -> str:
        return str(len(s)) + '#'

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
           encoded += self._metaLen(s) + s 
        return encoded
    
    def decode(self, s: str) -> List[str]:
        # Read the metadata length
        # Extract out the word
        # Repeat
        decoded = []
        metaLen = ''
        i = 0

        while i < len(s):
            c = s[i]
            if c != '#':
                metaLen += c
                i += 1
            else:
                length = int(metaLen)
                decoded.append(s[i + 1:i + 1 + length])
                i += 1 + length
                metaLen = ''
        
        return decoded


        

