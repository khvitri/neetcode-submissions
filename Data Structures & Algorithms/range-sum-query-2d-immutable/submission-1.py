class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

        self.prefixMatrix = [[0] for i in range(len(matrix) + 1)]
        self.prefixMatrix[0] = [0] * (len(matrix[0]) + 1)

        for row in range(len(matrix)):
            pSum = 0
            for col in range(len(matrix[0])):
                res = self.prefixMatrix[row][col + 1] + pSum + matrix[row][col]
                pSum += matrix[row][col]
                self.prefixMatrix[row + 1].append(res)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        pSum = self.prefixMatrix[r2][c2]        
        left = self.prefixMatrix[r2][c1 - 1] 
        top = self.prefixMatrix[r1 - 1][c2]
        diag = self.prefixMatrix[r1 - 1][c1 - 1]

        return pSum - left - top + diag


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)