from typing import List
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        iSeries=[]
        jSeries=[]
        answer=0
        rows,cols=len(grid),len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    iSeries.append(row)
                    jSeries.append(col)
                    
        if iSeries and jSeries:
            iSeries.sort()
            jSeries.sort()
            answer=(iSeries[-1]+1-iSeries[0])*(jSeries[-1]+1-jSeries[0])
        return answer

if __name__=="__main__":
    grid=[[0,1,0],[1,0,1]]
    print(Solution().minimumArea(grid=grid))