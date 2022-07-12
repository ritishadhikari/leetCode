class Solution():
    def numTrees(self,n:int) -> int:

        initialDict={1:1}
        for i in range(2,n+1):
            #perform action on i
            value=0
            for j in range(1,i+1):
                val1=initialDict[max(1,j-1)] 
                val2=initialDict[max(1,i-j)]  
                combination=val1*val2
                value+=combination
            initialDict[i]=value
        return initialDict[n]

if __name__=="__main__":
    n=6
    print(Solution().numTrees(n=n))