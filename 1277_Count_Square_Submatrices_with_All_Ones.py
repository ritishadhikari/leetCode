from typing import List
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row,column=len(matrix),len(matrix[0])
        ans=0
        for r in range(row):
            for c in range(column):
                if r and c and matrix[r][c]:
                    matrix[r][c]=min(matrix[r-1][c],matrix[r][c-1],matrix[r-1][c-1])+1
                ans+=matrix[r][c]
        return ans



if __name__=="__main__":
    matrix=[
        [0,1,1,1],
        [1,1,1,1],
        [0,1,1,1]
    ]
    print(Solution().countSquares(matrix=matrix))
