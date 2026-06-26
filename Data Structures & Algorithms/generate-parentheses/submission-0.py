class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        noOpen = n
        noClose = 0

        currPar = []
        def parenthesis() -> None:
            nonlocal noOpen, noClose
            
            if noOpen <= 0 and noClose <= 0:
                res.append(''.join(currPar))
                return
            
            if noClose <= 0:
                currPar.append('(')
                noOpen, noClose = noOpen - 1, noClose + 1
                parenthesis()
                noOpen, noClose = noOpen + 1, noClose - 1
                currPar.pop()
                return
            elif noOpen <= 0:
                currPar.append(')')
                noClose -= 1
                parenthesis()
                noClose += 1
                currPar.pop()
                return
            
            # Open parenthesis
            currPar.append('(') 
            noOpen, noClose = noOpen - 1, noClose + 1
            parenthesis()
            noOpen, noClose = noOpen + 1, noClose - 1
            currPar.pop()

            # Close parenthesis
            currPar.append(')')
            noClose -= 1
            parenthesis()
            noClose += 1
            currPar.pop()
        
        parenthesis()
        return res


