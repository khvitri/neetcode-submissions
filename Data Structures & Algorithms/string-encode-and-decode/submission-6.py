import base64

class Solution:
    # Base64 encode and use "," as the delimiter. "," is safe to use because b64 does
    # not have commas 

    def encode(self, strs: List[str]) -> str:
        # encode characters in base64
        if len(strs) == 1 and strs[0] == '':
            return ' '
        b64StrList = [base64.b64encode(bytes(s, 'utf-8')).decode('utf-8') for s in strs]
        return ','.join(b64StrList)

    def decode(self, s: str) -> List[str]:
        # decode the characters received
        if s == '':
            return []
        elif not s:
            return ['']
        b64StrList = s.split(',')
        return [base64.b64decode(b64Str).decode('utf-8') for b64Str in b64StrList]