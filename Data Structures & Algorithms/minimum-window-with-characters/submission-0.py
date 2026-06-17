class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        if len(t) == 0: return ""

        tCount = {}
        tInSCount = {}
        tContained = 0
        minWinSize = len(s) + 1
        res = ""

        for i in range(len(t)):
            tCount[t[i]] = 1 + tCount.get(t[i], 0)
        
        l = 0
        for r in range(0, len(s)):
            if minWinSize == len(t):
                return res
            
            if s[r] in tCount:
                tInSCount[s[r]] = 1 + tInSCount.get(s[r], 0)
                if tInSCount[s[r]] <= tCount[s[r]]:
                    tContained += 1

            while tContained == len(t):
                if r - l + 1 < minWinSize:
                    res = s[l : r + 1]
                    minWinSize = len(res)
                if s[l] in tCount: 
                    tInSCount[s[l]] -= 1 
                    if tInSCount[s[l]] < tCount[s[l]]:
                        tContained -= 1
                l += 1

        return res

            


        