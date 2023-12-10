from typing import List
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows,cols=len(matrix),len(matrix[0])
        transposedMatrix=[[0]*rows for c in range(cols)]
        for r in range(rows):
            for c in range(cols):
                transposedMatrix[c][r]=matrix[r][c]
        
        return transposedMatrix

if __name__=="__main__":
    matrix=[[1,2,3],[4,5,6],[7,8,9]]
    print(Solution().transpose(matrix=matrix))