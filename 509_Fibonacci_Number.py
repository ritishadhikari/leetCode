class Solution:
    def fib(self,n:int) -> int:
        count=0
        sumDict={}
        while count<=n:
            twoElementBack=count-2
            oneElementBack=count-1
            if twoElementBack<0:
                if oneElementBack<0:
                    sumDict[count]=0
                else: 
                    sumDict[count]=1
            else:
                sumDict[count]=sumDict[twoElementBack]+sumDict[oneElementBack]
            count+=1
        
        return sumDict[n]

if __name__=="__main__":
    n=5
    print(Solution().fib(n=n))