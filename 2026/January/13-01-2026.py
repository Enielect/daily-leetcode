# ∑
class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:
        # get total_area and y_max
        y_max, total_area = 0, 0
        for x, y, l in squares:
            total_area += l*l
            y_max = max(y_max, y + l)

        def validate_middle(y_m):
            area_y = 0
            for x, y, l in squares:
                if y < y_m:
                    area_y += min(l, y_m - y) * l
            return area_y * 2 >= total_area

        l, h, eps = 0, y_max, 1e-5
        while h - l > eps:
            mid = (h + l) / 2
            if validate_middle(mid):
                h = mid
            else:
                l = mid
        return h
    