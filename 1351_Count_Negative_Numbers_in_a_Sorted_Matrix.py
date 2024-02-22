# VVI
from typing import List
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
            l=0
            r=len(grid)-1
            c=0
            while r>=0 and c<len(grid[0]):
                if grid[r][c]<0: 
                    l+=len(grid[0])-c
                    r-=1
                else: c+=1
            return l

if __name__=="__main__":

    grid= \
    [
        [ 4,  3,  2, -1],
        [ 3,  2,  1, -2],
        [ 1, -2, -3, -4],
        [ 2, -3, -4, -5]
    ]	

    print(Solution().countNegatives(grid=grid))