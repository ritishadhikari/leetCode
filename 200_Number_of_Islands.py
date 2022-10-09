from typing import List
from collections import defaultdict
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row=len(grid)
        col=len(grid[0])
        count=0
        traceDict=defaultdict(lambda : [])
        up,down,left,right=[True]*4
        for i in range(row):
            for j in range(col):
                if int(grid[i][j]):
                    if i<row-1 and int(grid[i+1][j]):
                        traceDict[(i,j)].append((i+1,j))
                    if j<col-1 and int(grid[i][j+1]):
                        traceDict[(i,j)].append((i,j+1))
                    if j and int(grid[i][j-1]):
                        traceDict[(i,j)].append((i,j-1))
                    if i and int(grid[i-1][j]):
                        traceDict[(i,j)].append((i-1,j))  
                    # When all the Adjacent are Zero
                    if (i and not int(grid[i-1][j])) or not i:
                        up=False
                    if (j and not int(grid[i][j-1])) or not j:
                        left=False
                    if (j<col-1 and not int(grid[i][j+1])) or j==col-1:
                        right=False
                    if (i<row-1 and not int(grid[i+1][j])) or i==row-1:
                        down=False
                    if not down and not up and not right and not left:
                        traceDict[(i,j)].append(None) 
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
    grid = [["0","0","0","0","0","0","1"]]
    print(Solution().numIslands(grid=grid))
