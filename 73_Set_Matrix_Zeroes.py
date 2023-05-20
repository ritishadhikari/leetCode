from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        trace=set()
        rows=len(matrix)
        cols=len(matrix[0])

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]==0 and (r,c) not in trace:
                    trace.add((r,c))
                    for c2 in range(cols):
                        if matrix[r][c2]!=0:
                            trace.add((r,c2))
                            matrix[r][c2]=0
                    for r2 in range(rows):
                        if matrix[r2][c]!=0:
                            trace.add((r2,c))
                            matrix[r2][c]=0
        return matrix

if __name__=="__main__":
    matrix=[
        [0]
        ]
    print(Solution().setZeroes(matrix=matrix))