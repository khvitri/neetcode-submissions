class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        col = set()
        posDiag = set()
        negDiag = set()

        qPoses = [] # Queen's column by row order
        def backtrack() -> None:
            if n <= len(qPoses):
                board = []
                for qPos in qPoses:
                    row = '.' * qPos + 'Q' + '.' * (n - qPos - 1)
                    board.append(row)
                res.append(board)
                return
            
            r = len(qPoses)
            for c in range(n):
                posD, negD = r + c, r - c
                if (c in col or 
                  posD in posDiag or
                  negD in negDiag) :
                    continue
                
                col.add(c)
                posDiag.add(posD)
                negDiag.add(negD)
                qPoses.append(c)

                backtrack()

                col.remove(c)
                posDiag.remove(posD)
                negDiag.remove(negD)
                qPoses.pop()
        
        backtrack()
        return res
            


            