class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        sum = 0
        for idx,point in enumerate(points[1:]):
            y1, y2 = points[idx][1], point[1]
            x1, x2 = points[idx][0], point[0]
            
            sum += max(abs(x2-x1), abs(y2 - y1))
        return sum