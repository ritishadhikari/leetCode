from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        if len(matrix)==1 and len(matrix[0])==1:
            if matrix[0][0]=="1":
                return 1 
            else:
                return 0

        elif (len(matrix)>1 and len(matrix[0])==1) or (len(matrix)==1 and len(matrix[0])>1):
            for arr in matrix:
                for j in arr:
                    if j=="1":
                        return 1
            return 0
        else: 
            prevList=[]
            oneOffCase=0
            for i in range(len(matrix[0])-1):
                value=int(matrix[0][i])
                right=int(matrix[0][i+1])
                down=int(matrix[1][i])
                diagRight=int(matrix[1][i+1])

                if value and right and down and diagRight:
                    prevList.append(1)
                else: 
                    prevList.append(0)

                if value or right or down or diagRight:
                    oneOffCase=1          
            maxVal=max(prevList)
            
            for i in range(1,len(matrix)-1):
                presentList=[]
                for j in range(len(matrix[0])-1):
                    value=int(matrix[i][j])
                    top=prevList[j]
                    if not j:
                        left=0
                        diagLeft=0
                    else:
                        left=presentList[j-1]
                        diagLeft=prevList[j-1]
                    right=int(matrix[i][j+1])
                    down=int(matrix[i+1][j])
                    diagRight=int(matrix[i+1][j+1])
                    if value and right and down and diagRight:
                        minVal=min(top,left,diagLeft)
                        maxVal=max(maxVal,minVal+1)
                        presentList.append(minVal+1)
                    else:
                        presentList.append(0)

                    if value or right or down or diagRight:
                        oneOffCase=1
                prevList=presentList
            

            if  maxVal:
                return (maxVal+1)**2
            else: 
                return oneOffCase
        


if __name__=="__main__":
    mat= [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    # mat=[[1,1,0,1,0],[1,1,1,1,1],[1,1,1,1,1],[0,1,1,1,1],[0,1,1,1,1],[1,0,1,0,1]]
    mat=[["0","0","0"],["0","0","0"],["1","1","1"]]
    mat=[["0","1"],["1","0"]]
    print(Solution().maximalSquare(matrix=mat))