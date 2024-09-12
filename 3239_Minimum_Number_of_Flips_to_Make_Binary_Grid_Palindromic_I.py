from typing import List
class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        # Row Wise
        if cols%2:  maxCol=(cols//2)+1
        else:   maxCol=cols//2
        rowCount=0
        for r in range(rows):
            negativeC=-1
            for c in range(maxCol):
                if grid[r][c]!=grid[r][negativeC]: 
                    rowCount+=1
                negativeC-=1
        #colWise
        if rows%2:  maxRow=(rows//2)+1
        else:   maxRow=rows//2
        colCount=0
        for c in range(cols):
            negativeR=-1
            for r in range(maxRow):
                if grid[r][c]!=grid[negativeR][c]:
                    colCount+=1
                negativeR-=1
        return min(rowCount,colCount)


if __name__=="__main__":
    grid = [[1,0,0],[0,0,0],[0,0,1]]
    print(Solution().minFlips(grid=grid))