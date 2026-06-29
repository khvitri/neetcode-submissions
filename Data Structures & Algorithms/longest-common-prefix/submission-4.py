class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""

        prefix = strs[0]

        for i in range(1, len(strs)):
            s = strs[i]

            if len(s) < len(prefix):
                prefix = prefix[:len(s)]

            for j in range(0, len(s)):
                if (j >= len(prefix) or prefix[j] != s[j]):
                    prefix = prefix[:j]
                    break
                
            
            
         
        return prefix


