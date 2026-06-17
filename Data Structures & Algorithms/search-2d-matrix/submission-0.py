class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # First element in row closest to target and smaller than it
        bestRow = None
        leftRow, rightRow = 0, len(matrix) - 1
        while leftRow <= rightRow:
            midRow = (rightRow + leftRow) // 2
            if matrix[midRow][0] < target:
                leftRow = midRow + 1
                bestRow = matrix[midRow]
            elif matrix[midRow][0] > target:
                rightRow = midRow - 1
            else:
                return True
        
        if not bestRow:
            return False 
        
        leftCol, rightCol = 0, len(bestRow) - 1
        while leftCol <= rightCol: 
            midCol = (rightCol + leftCol) // 2
            if bestRow[midCol] < target:
                leftCol = midCol + 1
            elif bestRow[midCol] > target:
                rightCol = midCol - 1
            else:
                return True

        return False            
