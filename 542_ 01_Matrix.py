from typing import List
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if matrix:
            m=len(matrix)
        if matrix:
            n=len(matrix[0])
            
        for i in range(m):
            for j in range(n):
                if matrix[i][j]!=0:
                    matrix[i][j]=float('inf')
                    if i>0 and matrix[i-1][j]+1<matrix[i][j]:
                        matrix[i][j]=matrix[i-1][j]+1
                    if j>0 and matrix[i][j-1]+1<matrix[i][j]:
                        matrix[i][j]=matrix[i][j-1]+1
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if matrix[i][j]!=0:
                    if i<m-1 and matrix[i+1][j]+1<matrix[i][j]:
                        matrix[i][j]=matrix[i+1][j]+1
                    if j<n-1 and matrix[i][j+1]+1<matrix[i][j]:
                        matrix[i][j]=matrix[i][j+1]+1
       
        return matrix

if __name__=="__main__":
    matrix=[[0,0,1,0,1,1,1,0,1,1],
            [1,1,1,1,0,1,1,1,1,1],
            [1,1,1,1,1,0,0,0,1,1],
            [1,0,1,0,1,1,1,0,1,1],
            [0,0,1,1,1,0,1,1,1,1],
            [1,0,1,1,1,1,1,1,1,1],
            [1,1,1,1,0,1,0,1,0,1],
            [0,1,0,0,0,1,0,0,1,1],
            [1,1,1,0,1,1,0,1,0,1],
            [1,0,1,1,1,0,1,1,1,0]]

    # matrix=[[0,1,0],
    #         [0,1,0],
    #         [1,1,1]]
    print(Solution().updateMatrix(matrix=matrix))

