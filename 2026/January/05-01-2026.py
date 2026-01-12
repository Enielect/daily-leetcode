class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int | float:
        #okey seems like we got an idea.
        sum_, smallest = 0, float('inf')
        neg_count = 0
        for row in matrix:
            for col in row:
                sum_ += abs(col)
                smallest = min(smallest, abs(col))

                if col < 0:
                    neg_count +=1
        return sum_ if neg_count % 2 == 0 else (sum_ - smallest * 2)