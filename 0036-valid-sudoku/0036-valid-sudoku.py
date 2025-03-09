class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxs = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                value = board[row][col]
                membership = (row//3)*3 + (col//3)
                if value == '.': continue
                if value in rows[row] or value in  cols[col] or value in boxs[membership]: return False
                rows[row].add(value)
                cols[col].add(value)
                boxs[membership].add(value)
        return True
        