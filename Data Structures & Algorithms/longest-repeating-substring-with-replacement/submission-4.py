class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxRep = 0
        maxF = 0
        charCount = dict()
        l = 0
        for r in range(len(s)):
            charCount[s[r]] = 1 + charCount.get(s[r], 0)
            maxF = max(charCount[s[r]], maxF)

            # Shrink window from left side until replacements 
            # needed within window is lesser than or equal to K
            while (r - l + 1) - maxF > k:
                # Only keep track of max character count seen so
                # far because any lesser than that will not produce
                # produce a longer repeating character replacement 
                charCount[s[l]] -= 1
                l += 1 
            
            maxRep = max(r - l + 1, maxRep)
        
        return maxRep

            

