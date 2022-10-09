from typing import List
from collections import defaultdict
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row=len(grid)
        col=len(grid[0])
        count=0
        traceDict=defaultdict(lambda : [])
        for i in range(row):
            for j in range(col):
                up,down,left,right=[False]*4
                if int(grid[i][j]):
                    if i<row-1 and int(grid[i+1][j]):
                        traceDict[(i,j)].append((i+1,j))
                        down=True
                    if j<col-1 and int(grid[i][j+1]):
                        traceDict[(i,j)].append((i,j+1))
                        right=True
                    if j and int(grid[i][j-1]):
                        traceDict[(i,j)].append((i,j-1))
                        left=True
                    if i and int(grid[i-1][j]):
                        traceDict[(i,j)].append((i-1,j))  
                        up=True
                    # When all the Adjacent are Zero
                    if left+right+up+down==0:
                        count+=1
                   
        stack=[]
        for i in range(row):
            for j in range(col):
                if traceDict[(i,j)]:
                    count+=1
                    stack.append((i,j))
                    while stack:
                        val=stack.pop()
                        if traceDict[val]:
                            for index in traceDict[val]:
                                stack.append(index)
                            traceDict.pop(val)

        return count
if __name__=="__main__":
    grid = [["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]]
    print(Solution().numIslands(grid=grid))
