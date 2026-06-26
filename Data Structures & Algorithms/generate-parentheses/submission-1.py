class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        currPar = []
        def parenthesis(noOpen, noClose) -> None:
            
            if noOpen <= 0 and noClose <= 0:
                res.append(''.join(currPar))
                return
            
            if noClose <= 0:
                currPar.append('(')
                parenthesis(noOpen - 1, noClose + 1)
                currPar.pop()
                return
            elif noOpen <= 0:
                currPar.append(')')
                parenthesis(noOpen, noClose - 1)
                currPar.pop()
                return
            
            # Open parenthesis
            currPar.append('(') 
            parenthesis(noOpen - 1, noClose + 1)
            currPar.pop()

            # Close parenthesis
            currPar.append(')')
            parenthesis(noOpen, noClose - 1)
            currPar.pop()
        
        parenthesis(n, 0)
        return res


