from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        length=len(matrix)
        trace=set()
        achieved=False

        for i in range(length):
            for j in range(length):
                if len(trace)==length**2: 
                    achieved=True
                    break
                
                if (i,j) not in trace:
                    originalSwapI,originalSwapJ=(j,length-i-1)
                    secondSwapI,secondSwapJ=(originalSwapJ,length-originalSwapI-1)
                    thirdSwapI,thirdSwapJ=(secondSwapJ,length-secondSwapI-1)

                    secondHold=matrix[originalSwapI][originalSwapJ]
                    thirdHold=matrix[secondSwapI][secondSwapJ]
                    fourthHold=matrix[thirdSwapI][thirdSwapJ]

                    matrix[originalSwapI][originalSwapJ]=matrix[i][j]
                    matrix[secondSwapI][secondSwapJ]=secondHold
                    matrix[thirdSwapI][thirdSwapJ]=thirdHold
                    matrix[i][j]=fourthHold
                    
                    trace.add((originalSwapI,originalSwapJ))
                    trace.add((secondSwapI,secondSwapJ))
                    trace.add((thirdSwapI,thirdSwapJ))
                    trace.add((i,j))

            if achieved: 
                break

        return matrix

if __name__=="__main__":
    matrix=[
            [5,1,9,11],
            [2,4,8,10],
            [13,3,6,7],
            [15,14,12,16]
            ]
    print(Solution().rotate(matrix=matrix))