from typing import List
from math import inf
class Solution():
    def matrixBlockSum(self, mat=List[List[int]], k=int) -> List[List[int]]:
        maxCol=len(mat[0])
        answer=[[0]*maxCol for i in range(len(mat))]

        for i in range(len(mat)):
            startRow=max(0,i-k)
            endRow=min(len(mat),i+k+1)
            extractedMat=mat[startRow:endRow]
            for j in range(len(mat[0])):
                startCol=max(0,j-k)
                endCol=min(maxCol,j+k+1)
                s=0
                for arr in extractedMat:
                    s+=sum(arr[startCol:endCol])
                answer[i][j]=s
        return answer


if __name__=="__main__":
    mat=[[1,2,3],[4,5,6],[7,8,9]]
    print(Solution().matrixBlockSum(mat=mat,k=1))

