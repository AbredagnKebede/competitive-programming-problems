class Solution(object):
    def minimumTotal(self, triangle):
        bottomUp = [0]*(len(triangle) + 1)
        for row in triangle[::-1]:
            for ind, value in enumerate(row):
                bottomUp[ind] = value + min(bottomUp[ind], bottomUp[ind+1])
        return bottomUp[0]