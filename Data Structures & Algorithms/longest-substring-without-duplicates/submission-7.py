class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        l, r = 0, 1
        maxSubStr = 1
        seen = {s[l]}
        while r < len(s):
            if s[r] in seen:
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                l += 1
            seen.add(s[r])
            maxSubStr = max(maxSubStr, len(seen))
            r += 1
        
        return maxSubStr

        