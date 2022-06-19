from typing import List
from collections import deque

from pyparsing import col
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startColor=image[sr][sc]
        image[sr][sc]=color
        stack=deque([[sr,sc]])
        rows=len(image)
        cols=len(image[0])

        while stack:
            indexes=stack.popleft()
            x=indexes[0]
            y=indexes[1]

             # Sorting out x
            if x==rows-1:
                xNext=None
            else:
                xNext=x+1
            if x>0:
                xEarly=x-1
            else: 
                xEarly=None
            
            # Sorting out y
            if y==cols-1:
                yNext=None
            else:
                yNext=y+1
            if y>0:
                yEarly=y-1
            else: 
                yEarly=None
            
            if xEarly is not None:
                if image[xEarly][y]==startColor and image[xEarly][y]!=color:
                    image[xEarly][y]=color
                    stack.append([xEarly,y])
            if xNext is not None:
                if image[xNext][y]==startColor and image[xNext][y]!=color:
                    image[xNext][y]=color
                    stack.append([xNext,y])
            if yEarly is not None:
                if image[x][yEarly]==startColor and image[x][yEarly]!=color:
                    image[x][yEarly]=color
                    stack.append([x,yEarly])
            if yNext is not None:
                if image[x][yNext]==startColor and image[x][yNext]!=color:
                    image[x][yNext]=color
                    stack.append([x,yNext])
        
        return image
                       


if __name__=="__main__":
    image = [[0,0,0],[0,0,0]]   
    sr = 0
    sc = 0
    color = 0
    print(Solution().floodFill(image=image,sr=sr,sc=sc,color=color))