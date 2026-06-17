
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charFreqTracker = defaultdict(int)
        res = 1

        l = 0
        for r in range(len(s)):
            charFreqTracker[s[r]] += 1
            
            windowSize = r - l + 1
            mostFreq = max(charFreqTracker.values())
            while windowSize - mostFreq  > k:
                charFreqTracker[s[l]] -= 1
                l += 1
                windowSize = r - l + 1
            
            res = max(windowSize, res)
        
        return res
                


            
            
            
        
        