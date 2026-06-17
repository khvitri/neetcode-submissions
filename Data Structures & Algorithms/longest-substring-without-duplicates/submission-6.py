class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        l, r = 0, 1
        maxSubStr = 1
        seen = {s[l]}
        while r < len(s):
            if s[r] in seen:
                while l < r:
                    if s[l] == s[r]:
                        l += 1
                        break
                    seen.remove(s[l])
                    l += 1
            seen.add(s[r])
            maxSubStr = max(maxSubStr, len(seen))
            r += 1
        
        return maxSubStr

        