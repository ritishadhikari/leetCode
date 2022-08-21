from typing import List
class Solution:
    def spiralOrder(self,  matrix: List[List[int]]) -> List[int]:

        r=len(matrix)
        c=len(matrix[0])

        pointDict={
                   'right':{'op':'down','ra':'i+1','ca':'j-1'},
                   'down':{'op':'left','ra':'i-1','ca':'j-1'},
                   'left':{'op':'up','ra':'i-1','ca':'j+1'},
                   'up':{'op':'right','ra':'i+1','ca':'j+1'}
                  }

        finalList=[]
        finalLoc=set()
        
        i,j=0,0
        lastOp="right"
        while len(finalList)<r*c:
            if lastOp=="right":
                if j<c and (i,j) not in finalLoc:
                    finalList.append(matrix[i][j])
                    finalLoc.add((i,j))
                    j+=1
                else:
                    op=pointDict[lastOp]['op']
                    i=eval(pointDict[lastOp]['ra'])
                    j=eval(pointDict[lastOp]['ca'])
                    lastOp=op

            elif lastOp=="down":
                if i<r and (i,j) not in finalLoc:
                    finalList.append(matrix[i][j])
                    finalLoc.add((i,j))
                    i+=1
                else:
                    op=pointDict[lastOp]['op']
                    i=eval(pointDict[lastOp]['ra'])
                    j=eval(pointDict[lastOp]['ca'])
                    lastOp=op

            elif lastOp=="left":
                if j>=0 and (i,j) not in finalLoc:
                    finalList.append(matrix[i][j])
                    finalLoc.add((i,j))
                    j-=1
                else:
                    op=pointDict[lastOp]['op']
                    i=eval(pointDict[lastOp]['ra'])
                    j=eval(pointDict[lastOp]['ca'])
                    lastOp=op
            
            elif lastOp=="up":
                if i>=0 and (i,j) not in finalLoc:
                    finalList.append(matrix[i][j])
                    finalLoc.add((i,j))
                    i-=1
                else:
                    op=pointDict[lastOp]['op']
                    i=eval(pointDict[lastOp]['ra'])
                    j=eval(pointDict[lastOp]['ca'])
                    lastOp=op

        return finalList    

if __name__=="__main__":
    matrix = [
                [23,18,20,26,25],
                [24,22,3,4,4],
                [15,22,2,24,29],
                [18,15,23,28,28]
            ]
    print(Solution().spiralOrder(matrix=matrix))