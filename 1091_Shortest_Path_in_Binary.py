# VVI

from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rowCol=len(grid)
        if grid and (grid[0][0] or grid[rowCol-1][rowCol-1]):
            return -1
        else:
            queue=deque()
            queue.append((0,0,1))
            seen=set()
            seen.add((0,0))
            dirs=[  
                    (1,-1),  # downleft
                    (1,1),  # downright
                    (-1,0), # down
                    (0,1),  # right
                    (0,-1),  # left
                    (-1,-1), # topleft
                    (-1,1),  # topright
                    (1,0), # top
                ]
            while queue:
                i,j,count=queue.popleft()
                if i==rowCol-1 and j==rowCol-1:
                    return count
                for dir in dirs:
                    x=dir[0]+i
                    y=dir[1]+j
                    if 0<=x<rowCol and 0<=y<rowCol:
                        if (x,y) not in seen and not grid[x][y]:
                            seen.add((x,y))
                            queue.append((x,y,count+1))
            return -1

                
if __name__=="__main__":
    grid=[
            [0,1,0,1,0],
            [1,0,0,0,1],
            [0,0,1,1,1],
            [0,0,0,0,0],
            [1,0,1,0,0]
        ]

    # grid=[
    #     [0,	0,	0,	1],
	#     [0,	0,	1,	0],
	#     [1,	0,	1,	0],
	#     [1,	1,	1,	0],
    #     ]
    print(Solution().shortestPathBinaryMatrix(grid=grid))