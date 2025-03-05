class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])

        arrows, prev = 1, points[0][1]
        for i in range(1,len(points)):
            start, end = points[i]

            if prev < start:
                arrows += 1
                prev = end

        return arrows
