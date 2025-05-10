class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        main_diag =  defaultdict(list)
        ans = []
        n, m = len(mat), len(mat[0])
        for i in range(n):
            for j in range(m):
                main_diag[i+j].append(mat[i][j])
        for i in main_diag:
            if i%2 == 0:
                ans.extend(main_diag[i][::-1])
            else:
                ans.extend(main_diag[i])
        return ans

