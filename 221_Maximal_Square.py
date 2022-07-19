from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        prevList=[int(val) for val in matrix[0]]
        maxVal=max(prevList)
        for i in range(1,len(matrix)):
            presentList=[]
            for j in range(len(matrix[0])):
                if not j:
                    maxVal=max(maxVal,int(matrix[i][j]))
                    presentList.append(int(matrix[i][j]))
                else:
                    if not int(matrix[i][j]):
                        presentList.append(0)
                    else:
                        left=presentList[j-1]
                        up=prevList[j]
                        diagLeft=prevList[j-1]
                        if left and up and diagLeft:
                            if left==up and up==diagLeft:
                                maxVal=max(maxVal,left+1)
                                presentList.append(left+1)
                            else:
                                maxVal=max(maxVal,min(left,up,diagLeft)+1)
                                presentList.append(min(left,up,diagLeft)+1)
                        else:
                            maxVal=max(maxVal,1)
                            presentList.append(1)
            prevList=presentList
        return maxVal**2
        


if __name__=="__main__":
    mat= [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    # mat=[[1,1,0,1,0],[1,1,1,1,1],[1,1,1,1,1],[0,1,1,1,1],[0,1,1,1,1],[1,0,1,0,1]]
    # mat=[["0","0","0"],["0","0","0"],["1","1","1"]]
    # mat=[["0","1"],["1","0"]]
    mat=[["1","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"],["1","1","1","1","1"],["0","0","1","1","1"]]
    print(Solution().maximalSquare(matrix=mat))