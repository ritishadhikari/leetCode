from typing import List
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        row=len(heights)
        col=len(heights[0])
        finalList=[]

        for r in range(row):
            for c in range(col):  
                val=heights[r][c] 
                # Atlantic Case
                atlanticCase=True
                if r!=row-1 and c!=col-1:
                    distanceRight=col-1-c
                    distanceDown=row-1-r
                    if distanceRight>=distanceDown:  # go down first
                        for l in range(r+1,row):
                            if heights[l][c]>val:
                                atlanticCase=False
                                break
                        if not atlanticCase:  # then go right
                            atlanticCase=True
                            for k in range(c+1,col):
                                if heights[r][k]>val:
                                    atlanticCase=False
                                    break
                    else:  # go right first
                        for k in range(c+1,col):
                                if heights[r][k]>val:
                                    atlanticCase=False
                                    break
                        if not atlanticCase:  # then go down
                            atlanticCase=True
                            for l in range(r+1,row):
                                if heights[l][c]>val:
                                    atlanticCase=False
                                    break
                            
                # Pacific Case
                pacificCase=True
                if r and c:
                    distanceLeft=c
                    distanceTop=r
                    if distanceLeft>=distanceTop:  # go top first
                        for l in range(r-1,-1,-1):
                            if heights[l][c]>val:
                                pacificCase=False
                                break
                        if not pacificCase:  # then go down
                            pacificCase=True
                            for k in range(c-1,-1,-1):
                                if heights[r][k]>val:
                                    pacificCase=False
                                    break
                    
                    else:  # go down first
                        for k in range(c-1,-1,-1):
                                if heights[r][k]>val:
                                    pacificCase=False
                                    break
                        if not pacificCase:  # then go top  
                            pacificCase=True  
                            for l in range(r-1,-1,-1):
                                if heights[l][c]>val:
                                    pacificCase=False
                                    break

                if atlanticCase and pacificCase:
                    finalList.append([r,c])

        return finalList







if __name__=="__main__":
    heights = [ 
                [1,2,2,3,5],
                [3,2,3,4,4],
                [2,4,5,3,1],
                [6,7,1,4,5],
                [5,1,1,2,4]
                ]
    print(Solution().pacificAtlantic(heights=heights))