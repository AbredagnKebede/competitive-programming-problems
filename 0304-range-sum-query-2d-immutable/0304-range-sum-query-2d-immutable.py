class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self._2d = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            cur = 0
            for j in range(len(matrix[0])):
                cur += matrix[i][j]
                self._2d[i][j] = cur 

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        mat_sum = 0
        for i in range(row1, row2+1): 
            if col1 == 0:
                mat_sum += self._2d[i][col2]  
            else:
                mat_sum += self._2d[i][col2] - self._2d[i][col1-1]
           
        return mat_sum



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)