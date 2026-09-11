class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        keyToIdx = {}

        for i in range(len(keyboard)):
            keyToIdx[keyboard[i]] = i
        
        res, curPos = 0, 0
        for c in word:
            charPos = keyToIdx[c]
            res += abs(charPos - curPos)
            curPos = charPos
        
        return res


