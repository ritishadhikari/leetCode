from typing import List
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        collections={}
        row,col=len(grid2),len(grid2[0])
        count=0
        for i in range(row):
            for j in range(col):
                if grid2[i][j]:
                    left,right,top,down=[False]*4
                    if j and grid2[i][j-1]:  # left
                        if (i,j) not in collections: collections[(i,j)] = [(i,j-1)]
                        else: collections[(i,j)].append((i,j-1))
                        left=True
                    if j<col-1 and grid2[i][j+1]:  # right
                        if (i,j) not in collections: collections[(i,j)] = [(i,j+1)]
                        else: collections[(i,j)].append((i,j+1))
                        right=True
                    if i and grid2[i-1][j]:  # top
                        if (i,j) not in collections: collections[(i,j)] = [(i-1,j)]
                        else: collections[(i,j)].append((i-1,j))
                        top=True
                    if i<row-1 and grid2[i+1][j]:  # down
                        if (i,j) not in collections: collections[(i,j)] = [(i+1,j)]
                        else: collections[(i,j)].append((i+1,j))
                        down=True
                    if not (left+right+top+down) and grid1[i][j]:
                        count+=1
        for i in range(row):
            for j in range(col):
                if (i,j) in collections:
                    grid1Presence=True
                    stack=set()
                    stack.add((i,j))
                    while stack:
                        index=stack.pop()
                        if not grid1[index[0]][index[1]] and grid1Presence:
                                grid1Presence=False
                        if index in collections:
                            stack.update(collections[index])
                            collections.pop(index)
                    if grid1Presence:
                        count+=1
        return count



if __name__=="__main__":
    grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]]
    grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
    print(Solution().countSubIslands(grid1=grid1, grid2=grid2))