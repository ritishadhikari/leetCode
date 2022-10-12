from typing import List
from collections import defaultdict
class Solution:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        row=len(grid)
        col=len(grid[0])
        count=0
        traceDict={}
        isolatedIslandOccurred=False
        for i in range(row):
            for j in range(col):
                up,down,left,right=[False]*4
                if int(grid[i][j]):
                    if i<row-1 and int(grid[i+1][j]):
                        if (i,j) in traceDict.keys():
                            traceDict[(i,j)].append((i+1,j))
                        else:
                            traceDict[(i,j)]=[(i+1,j)]
                        down=True
                    if j<col-1 and int(grid[i][j+1]):
                        if (i,j) in traceDict.keys():
                            traceDict[(i,j)].append((i,j+1))
                        else:
                            traceDict[(i,j)]=[(i,j+1)]
                        right=True
                    if j and int(grid[i][j-1]):
                        if (i,j) in traceDict.keys():
                            traceDict[(i,j)].append((i,j-1))
                        else:
                            traceDict[(i,j)]=[(i,j-1)]
                        left=True
                    if i and int(grid[i-1][j]):
                        if (i,j) in traceDict.keys():
                            traceDict[(i,j)].append((i-1,j))  
                        else:
                            traceDict[(i,j)]=[(i-1,j)]
                        up=True
                    # When all the Adjacent are Zero
                    if left+right+up+down==0 and not isolatedIslandOccurred:
                        isolatedIslandOccurred=True
                        count=1
                   
        stack=[]
        for i in range(row):
            for j in range(col):
                if (i,j) in traceDict.keys():
                    stack.append((i,j))
                    tempCount=0
                    while stack:
                        val=stack.pop()
                        if val in traceDict:
                            stack.extend(traceDict[val])
                            traceDict.pop(val)
                            tempCount+=1
                    count=max(count,tempCount)

        return count
if __name__=="__main__":
    grid = [
            [0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]
            ]
    print(Solution().maxAreaOfIsland(grid=grid))
