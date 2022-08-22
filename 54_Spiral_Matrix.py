from typing import List
class Solution:
    def spiralOrder(self,  matrix: List[List[int]]) -> List[int]:

        r=len(matrix)
        c=len(matrix[0])

        finalDict={}
           
        cond2='(i,j) not in finalDict'
        pointDict={
                    'right':{'normalCond1':'j<c', 'normalCond2': cond2, 'iNorm':'i','jNorm': 'j+1', 'op':'down', 'ra':'i+1', 'ca':'j-1'},
                    'down':{'normalCond1': 'i<r','normalCond2': cond2, 'iNorm': 'i+1', 'jNorm': 'j' ,'op':'left', 'ra':'i-1', 'ca':'j-1'},  
                    'left':{'normalCond1': 'j>=0', 'normalCond2': cond2, 'iNorm': 'i', 'jNorm': 'j-1', 'op':'up','ra':'i-1', 'ca':'j+1'},  
                    'up':{'normalCond1':'i>=0', 'normalCond2': cond2, 'iNorm': 'i-1', 'jNorm': 'j', 'op':'right','ra':'i+1','ca':'j+1'}
                  }

        i,j=0,0
        lastOp="right"
        while len(finalDict)<r*c:
            if eval(pointDict[lastOp]['normalCond1']) and eval(pointDict[lastOp]['normalCond2']):
                finalDict[(i,j)]=matrix[i][j]
                i=eval(pointDict[lastOp]['iNorm'])
                j=eval(pointDict[lastOp]['jNorm'])
            else:
                op=pointDict[lastOp]['op']
                i=eval(pointDict[lastOp]['ra'])
                j=eval(pointDict[lastOp]['ca'])
                lastOp=op

        return list(finalDict .values())  

if __name__=="__main__":
    matrix = [
                [23,18,20,26,25],
                [24,22,3,4,4],
                [15,22,2,24,29],
                [18,15,23,28,28]
]
    print(Solution().spiralOrder(matrix=matrix))