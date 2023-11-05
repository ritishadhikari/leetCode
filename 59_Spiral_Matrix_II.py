# VVI
from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        numbers=(i for i in range(1,n**2+1))
        left,right=0,n-1
        top,down=0,n-1
        matrix=[[0]*n for i in range (n)]

        while left<=right and top<=down:

            for col in range(left,right+1):
                matrix[top][col]=next(numbers)
            top+=1

            for row in range(top,down+1):
                matrix[row][right]=next(numbers)
            right-=1

            for col in range(right,left-1,-1):
                matrix[down][col]=next(numbers)
            down-=1

            for row in range(down,top-1,-1):
                matrix[row][left]=next(numbers)
            left+=1
        
        return matrix


if __name__=="__main__":
    n=4
    print(Solution().generateMatrix(n=n))