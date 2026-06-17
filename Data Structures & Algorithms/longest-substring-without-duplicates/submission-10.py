class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # l = 2
        # r = 4
        # Set: {'y', 'z', 'x'}

        maxSubStr = 0
        winSeen = set()
        l = 0
        for r in range(len(s)):
            while s[r] in winSeen:
                winSeen.remove(s[l])
                l += 1
            winSeen.add(s[r])
            maxSubStr = max(len(winSeen), maxSubStr)
        
        return maxSubStr

