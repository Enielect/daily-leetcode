from math import sqrt

class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:

        def divisor(n):
            count, sum = 0, 0
            for i in range(1, int(sqrt(n)) + 1):
                if n % i == 0:
                    sum += i
                    count += 1
                    if i * i != n:
                        sum += n // i
                        count += 1

            return count, sum

        res = 0
        for num in nums:
            count, sum = divisor(num)
            if count == 4:
                res += sum

        return res