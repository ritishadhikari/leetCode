from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[None] * n for _ in range(0, n)]
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        numbers = (i for i in range(1, n ** 2 + 1))
        while left <= right and top <= bottom:

            for col in range(left, right + 1):
                matrix[top][col] = next(numbers)
            top += 1

            for row in range(top, bottom + 1):
                matrix[row][right] = next(numbers)
            right -= 1

            for col in range(right, left - 1, -1):
                matrix[bottom][col] = next(numbers)
            bottom -= 1

            for row in range(bottom, top - 1, -1):
                matrix[row][left] = next(numbers)
            left += 1

        return matrix    

if __name__=="__main__":
    n=4
    print(Solution().generateMatrix(n=n))