class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        transform = int(''.join([str(x) for x in digits])) + 1
        return [int(x) for x in str(transform)]
    
class Solution1:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] +=1
                return digits

        return [1] + digits