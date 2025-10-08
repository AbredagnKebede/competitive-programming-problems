class Solution:
    def returnRow1(self, grid):
        return grid.pop(0)
    
    def returnLastcol(self, grid):
        last_col = len(grid[0]) - 1
        vals = []
        for i in range(len(grid)):
            vals.append(grid[i].pop(last_col))
        return vals
    
    def returnCol1(self, grid):
        vals = []
        for i in range(len(grid)):
            vals.append(grid[i].pop(0))
        return vals[::-1]
    
    def returnLastrow(self, grid):
        return grid.pop()[::-1]  

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        while matrix:
            ans.extend(self.returnRow1(matrix))   # Removes top row
            if matrix and matrix[0]:  # Check if matrix still has elements
                ans.extend(self.returnLastcol(matrix))  # Removes last column
            if matrix and matrix[0]: 
                ans.extend(self.returnLastrow(matrix))  # Removes last row
            if matrix and matrix[0]:  
                ans.extend(self.returnCol1(matrix))  # Removes first column
        return ans
