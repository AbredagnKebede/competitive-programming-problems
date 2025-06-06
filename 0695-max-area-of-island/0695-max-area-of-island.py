class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(r, c):
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                grid[r][c] == 0 or visited[r][c]):
                return 0

            visited[r][c] = True
            area = 1  
 
            area += dfs(r+1, c)
            area += dfs(r-1, c)
            area += dfs(r, c+1)
            area += dfs(r, c-1)

            return area

        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and not visited[r][c]:
                    max_area = max(max_area, dfs(r, c))

        return max_area
        