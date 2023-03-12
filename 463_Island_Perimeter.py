from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])

        def isIsland(r,c):
            if r>=0 and r<=row-1 and c>=0 and c<=col-1:
                if grid[r][c]==1: 
                    return True
                else:
                    return False
            return False 
            
        count=0
        for rnum in range(row):
            for cnum in range(col):
                if grid[rnum][cnum]: 
                    if not isIsland(r=rnum,c=cnum-1):  # left
                        count+=1
                    if not isIsland(r=rnum,c=cnum+1):  # right
                        count+=1
                    if not isIsland(r=rnum-1,c=cnum):  # up
                        count+=1
                    if not isIsland(r=rnum+1, c=cnum):  # down
                        count+=1
        return count
                

if __name__=="__main__":
    grid = [[1,0]]
    print(Solution().islandPerimeter(grid=grid))