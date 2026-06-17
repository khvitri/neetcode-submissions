
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxCount = 0
        charCount = defaultdict(int)
        res = 1

        l = 0
        for r in range(len(s)):
            charCount[s[r]] += 1
            maxCount = max(charCount[s[r]], maxCount)
            while (r - l + 1) - maxCount > k:
                charCount[s[l]] -= 1
                l += 1
            
            res = max(r - l + 1, res)
        
        return res
                


            
            
            
        
        