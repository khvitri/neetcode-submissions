class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        bestRow = None

        while l <= r:
            m = (l + r) // 2

            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][0] < target:
                l = m + 1
                bestRow = matrix[m]
            else:
                return True
        
        if not bestRow:
            return False

        l, r = 0, len(bestRow) - 1
        while l <= r:
            m = (l + r) // 2
            
            if bestRow[m] > target:
                r = m - 1
            elif bestRow[m] < target:
                l = m + 1
            else:
                return True
        
        return False