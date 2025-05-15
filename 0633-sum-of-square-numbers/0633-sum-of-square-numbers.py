class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left_boundary = 1
        right_boundary  = int(sqrt(c))
        if sqrt(c) == right_boundary:
            return True
        while left_boundary <= right_boundary:
            if left_boundary**2 + right_boundary**2 == c:
                return True 
            elif left_boundary**2 + right_boundary**2 < c:
                left_boundary +=1
            else:
                right_boundary -=1
        return False


        
