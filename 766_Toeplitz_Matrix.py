from typing import List
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row=len(matrix)
        col=len(matrix[0])
        for i in range(row):
            for j in range(col):
                x,y=i+1,j+1
                if 0<x<row and 0<y<col:
                    if matrix[i][j]!=matrix[x][y]: return False
        return True

if __name__=="__main__":
    matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
    print(Solution().isToeplitzMatrix(matrix=matrix))