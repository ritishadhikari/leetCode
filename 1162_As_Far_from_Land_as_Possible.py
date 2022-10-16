from typing import List

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        oneDict={}
        zeroDict={}
        row,col=len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if not grid[i][j]:
                    # If Left is 1
                    if j and grid[i][j-1]:
                        if (i,j) not in oneDict:    oneDict[(i,j)]=set()
                        oneDict[(i,j)].add((i,j-1))
                    # If Left is 0
                    elif j and not grid[i][j-1]:
                        if (i,j) not in zeroDict:    zeroDict[(i,j)]=set()
                        zeroDict[(i,j)].add((i,j-1))
                    # If Right is 1
                    if j<col-1 and grid[i][j+1]:
                        if (i,j) not in oneDict:    oneDict[(i,j)]=set()
                        oneDict[(i,j)].add((i,j+1))
                    # If Right is 0
                    elif j<col-1 and not grid[i][j+1]:
                        if (i,j) not in zeroDict:    zeroDict[(i,j)]=set()
                        zeroDict[(i,j)].add((i,j+1))
                    # If Top is 1
                    if i and grid[i-1][j]:
                        if (i,j) not in oneDict:    oneDict[(i,j)]=set()
                        oneDict[(i,j)].add((i-1,j))
                    # If Top is 0
                    elif i and not grid[i-1][j]:
                        if (i,j) not in zeroDict:    zeroDict[(i,j)]=set()
                        zeroDict[(i,j)].add((i-1,j))
                    # If Down is 1
                    if i<row-1 and grid[i+1][j]:
                        if (i,j) not in oneDict:    oneDict[(i,j)]=set()
                        oneDict[(i,j)].add((i+1,j))
                    # If Down is 0
                    elif i<row-1 and not grid[i+1][j]:
                        if (i,j) not in zeroDict:    zeroDict[(i,j)]=set()
                        zeroDict[(i,j)].add((i+1,j))

        countDict={key:1 for key in oneDict.keys()}
        
        for key in zeroDict:
            stack=set()
            stack.add(key)
            tmpDict=zeroDict.copy()
            while stack:
                index=stack.pop()
                if index not in oneDict:
                    if index in tmpDict:
                        stack.update(tmpDict[index])
                        tmpDict.pop(index)
                else:
                    maxDistance=0
                    for loc in oneDict[index]:
                        distance=abs(loc[0]-key[0])+abs(loc[1]-key[1])
                        maxDistance=max(maxDistance,distance)
                        if key not in oneDict: oneDict[key]=set()
                        oneDict[key].add((loc))
                    countDict[key]=maxDistance
        # return countDict
        if (countDict and max(countDict.values())==0) or not countDict:
            return -1
        else:   
            return max(countDict.values()) 

        



if __name__=="__main__":
    grid=[[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
    print(Solution().maxDistance(grid=grid))