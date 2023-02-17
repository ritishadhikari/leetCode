from typing import List
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        length=len(mat)

        def getNextRowCol(r,c,):
            return c,length-r-1
        
        def rotateImage(matrix):
            seen=set()
            for i in range(length):
                for j in range(length):
                    if (i,j) not in seen:
    
                        r,c=getNextRowCol(r=i,c=j) # getting first row last col
                        k=matrix[r][c]  # storing value of first row last col
                        matrix[r][c]=matrix[i][j]  # assigning original value to first row last col
                        seen.add((r,c))  # adding first row last col to seen
                        
                        r,c=getNextRowCol(r=r,c=c)  # getting last row last col
                        k,matrix[r][c]=matrix[r][c],k
                        seen.add((r,c))  # adding last row last col to seen
                        
                        r,c=getNextRowCol(r=r,c=c)  # getting last row fist col
                        k,matrix[r][c]=matrix[r][c],k
                        seen.add((r,c))  # adding last row last col to seen

                        r,c=getNextRowCol(r=r,c=c)  # Getting original row and col
                        k,matrix[r][c]=matrix[r][c],k
                        seen.add((r,c))  # adding original row original col to seen
            return matrix
        
        i=0
        while i<4:
            rotatedImage=rotateImage(matrix=mat)
            if rotatedImage==target: return True
            i+=1
        return False

if __name__=="__main__":
    mat = [[0,0,0],[0,0,1],[0,0,1]]
    target = [[0,0,0],[0,0,1],[0,0,1]]
    print(Solution().findRotation(mat=mat,target=target))
    