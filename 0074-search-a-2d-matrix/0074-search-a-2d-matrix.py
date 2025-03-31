class Solution(object):
    def searchMatrix(self, matrix, target):
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (l+r)//2
            if target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][-1]:
                l = mid + 1
            else:
                return target in matrix[mid]
        return False
        