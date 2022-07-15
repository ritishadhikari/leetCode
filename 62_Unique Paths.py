class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        evalMat=[[0 for i in range(n+1)] for j in range(m+1)]

        for i in range(m):
            for j in range(n):
                aboveIndexVal=evalMat[i][j+1]
                leftIndexVal=evalMat[i+1][j]

                # Multiplicative    
                s=0
                if i<m-1:
                    s+=1
                if j<n-1:
                    s+=1
                multiplicativeVal=max(1,s)

                # Addidive
                if i<m-1:
                    leftIndexVal=leftIndexVal//2
                
                if j<n-1:
                    aboveIndexVal=aboveIndexVal//2
                
                addidiveVal=max(1,aboveIndexVal+leftIndexVal)

                evalMat[i+1][j+1]=multiplicativeVal*addidiveVal


        return evalMat[m][n]


if __name__=="__main__":
    m=3
    n=2
    print(Solution().uniquePaths(m=m,n=n))