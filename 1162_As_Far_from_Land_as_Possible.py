# VVI
from typing import List

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        row, col=len(grid),len(grid[0])
        collections=set()

        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    collections.add((i,j))
        iter=-1
        while collections:
            iter+=1
            ns=set()
            for index in collections:
                i,j=index
                # Left Check
                if j and not grid[i][j-1]:
                    grid[i][j-1]=1
                    ns.add((i,j-1))
                # Right Check
                if j<col-1 and not grid[i][j+1]:
                    grid[i][j+1]=1
                    ns.add((i,j+1))
                # Top Check
                if i and not grid[i-1][j]:
                    grid[i-1][j]=1
                    ns.add((i-1,j))
                # Down Check
                if i<row-1 and not grid[i+1][j]:
                    grid[i+1][j]=1
                    ns.add((i+1,j))

            collections=ns
        return -1 if iter<=0 else iter


if __name__=="__main__":
    grid=[
            [1,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,1,0,0],
            [1,1,0,1,0,1,1,1,1,1,1,1,0,1,0,0,0,1,1,1],
            [0,0,1,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0],
            [0,0,1,1,0,0,0,1,1,1,1,0,1,1,1,0,0,1,0,1],
            [1,0,1,1,0,1,1,1,0,1,0,1,0,1,1,0,1,0,1,0],
            [0,0,1,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,1],
            [0,0,0,1,0,0,1,1,0,0,1,1,1,1,0,0,0,0,1,0],
            [1,0,0,1,0,1,1,0,0,1,0,0,1,0,1,1,1,0,0,1],
            [0,1,0,1,1,0,0,1,1,1,1,1,0,0,1,0,1,0,0,0],
            [1,0,1,0,0,0,0,0,0,1,1,1,0,0,1,0,1,0,1,0],
            [0,1,1,0,1,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0],
            [0,0,1,1,1,1,1,1,1,0,0,0,1,0,0,0,0,0,1,0],
            [0,0,1,1,0,0,1,1,1,1,1,1,1,0,1,0,1,0,0,0],
            [0,1,0,1,0,0,0,1,1,1,0,0,0,1,1,0,0,1,0,1],
            [1,0,0,0,1,0,1,0,1,1,1,1,0,0,1,0,0,0,1,1],
            [0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],
            [0,1,0,1,0,0,0,1,0,1,1,1,1,1,0,0,0,0,0,1],
            [1,1,1,0,0,1,0,1,1,0,0,0,0,1,1,0,0,0,1,0],
            [1,1,1,1,1,1,0,1,0,0,0,1,1,1,1,0,0,1,0,1],
            [0,0,0,1,1,0,1,0,1,0,1,0,1,1,0,1,0,0,0,0]
            ]


    print(Solution().maxDistance(grid=grid))