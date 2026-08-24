class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        ROWS = len(words)

        for i in range(ROWS):
            rowS = words[i]
            colS = []

            for j in range(ROWS):
                if i < len(words[j]):
                    colS.append(words[j][i])
            
            colS = "".join(colS)

            if rowS != colS:
                return False
        
        return True


