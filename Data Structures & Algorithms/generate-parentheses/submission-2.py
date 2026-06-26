class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        currPar = []
        def parenthesis(noOpen, noClose) -> None:
            
            if noOpen == noClose == n:
                res.append(''.join(currPar))
                return
            
            if noOpen < n:
                currPar.append('(')
                parenthesis(noOpen + 1, noClose)
                currPar.pop()
            
            if noClose < noOpen:
                currPar.append(')')
                parenthesis(noOpen, noClose + 1)
                currPar.pop()
        
        parenthesis(0, 0)
        return res


