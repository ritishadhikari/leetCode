from typing import List
from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        traceDict={}
        row=col=len(grid)
        dirs=[(0,-1),(0,1),(-1,0),(1,0)]
        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    count=0
                    for dir in dirs:
                        x=dir[0]+i
                        y=dir[1]+j
                        if 0<=x<=row-1 and 0<=y<=col-1 and grid[x][y]:
                            if (i,j) not in traceDict: traceDict[(i,j)]=set()
                            traceDict[(i,j)].add((x,y))
                            count+=1
                    if count==0: traceDict[(i,j)]=None
                        
        islandCollections={1:set(),2:set()}
        stack=set()
        for i in range(row):
            for j in range(col):
                if (i,j) in traceDict:
                    stack.add((i,j))
                    if not islandCollections[1]:
                        islandToConsider=1
                    else: islandToConsider=2
                    while stack:
                        land=stack.pop()
                        if land in traceDict:
                            islandCollections[islandToConsider].add(land)
                            if traceDict[land] is not None: stack.update(traceDict[land])
                            traceDict.pop(land)

        # Once we find the islands, we need to reach the second island from the 
        # first island, and for that we need to make the adjacent water as
        # the land by doing BFS.  
        getCountDict=set()
        while islandCollections[1]:
            ns=set()
            for land in islandCollections[1]:
                i,j=land
                if land not in getCountDict: getCountDict.add(land)
                dirs=[(0,-1),(0,1),(-1,0),(1,0)]
                for dir in dirs:
                    x=dir[0]+i
                    y=dir[1]+j
                    if 0<=x<=row-1 and 0<=y<=col-1 and (x,y) not in getCountDict:
                        if grid[x][y]:
                            if (x,y) in islandCollections[2]:
                                return grid[i][j]-1
                        else:
                            ns.add((x,y))
                            grid[x][y]=grid[i][j]+1
                            getCountDict.add((x,y))
            islandCollections[1]=ns


if __name__=="__main__":
    grid=[[0,1,0],[0,0,0],[0,0,1]]
    print(Solution().shortestBridge(grid=grid))