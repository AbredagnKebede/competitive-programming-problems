class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        mx_sum = 0
        for i in range(len(grid)):
            mx_row = max(grid[i])
            for j in range(len(grid)):
                mx_col = 0
                for k in range(len(grid)):
                    mx_col = max(mx_col, grid[k][j])
                
                need = min(mx_row, mx_col)
                mx_sum += (need - grid[i][j])
        return mx_sum



