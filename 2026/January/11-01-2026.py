class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # formula = heights[i] * (j - i - 1)
        stack, max_area = [(-1, 0)], 0
        for right, height in enumerate(heights):
            while stack and height < stack[-1][1]:
                _, val = stack.pop()
                max_area = max(val * (right - stack[-1][0] - 1), max_area)
            stack.append((right, height))

        for idx, height in stack:
            max_area = max(max_area, height * (len(heights) - idx))
        return max_area


# print(Solution().largestRectangleArea([2,1,5,6,2,3]))
# print(Solution().largestRectangleArea([2,4]))

# PRev bad pythonic solution

class Solution1:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        # generate histogram
        n, m, = len(matrix), len(matrix[0])
        histogram, max_area = [0] * m, 0
        for i in range(n):
            stack = [(-1, 0)]
            for j in range(m):
                cur, cur_histogram = int(matrix[i][j]), histogram[j]
                histogram[j] = cur_histogram + 1 if cur != 0 else 0
            for right, height in enumerate(histogram):
                while stack and height < stack[-1][1]:
                    _, cur = stack.pop()
                    max_area = max(max_area, cur * (right - stack[-1][0] - 1))
                stack.append((right, height))
            for idx, height in enumerate(stack[1:]):
                _, cur_height = height
                max_area = max(max_area, cur_height * (m - stack[idx][0] - 1))
        return max_area
    
# Better written SOlution, same logic

class Solution2:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        cols = len(matrix[0])
        histogram, max_area = [0] * cols, 0

        for row in matrix:
            stack = [(-1, 0)]
            histogram = [h + 1 if val == "1" else 0 for h, val in zip(histogram, row)]

            for right, height in enumerate(histogram):
                while stack and height < stack[-1][1]:
                    _, popped_height = stack.pop()
                    width = right - stack[-1][0] - 1
                    max_area = max(max_area, popped_height * width)
                stack.append((right, height))

            for idx, (_, height) in enumerate(stack[1:]):
                width = cols - stack[idx][0] - 1
                max_area = max(max_area, height * width)

        return max_area


print(Solution1().maximalRectangle([["1", "0"], ["1", "0"]]))
