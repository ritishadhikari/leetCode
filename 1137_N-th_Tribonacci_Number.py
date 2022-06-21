class Solution:
    def tribonacci(self, n: int) -> int:
        sumDict={}
        count=0
        while count<=n:
            thirdLastVal=count-3
            secondLastVal=count-2
            lastVal=count-1
            if secondLastVal<0:
                sumDict[count]=count
            elif secondLastVal==0:
                sumDict[count]=sumDict[secondLastVal]+sumDict[lastVal]
            else:
                sumDict[count]=sumDict[thirdLastVal]+sumDict[secondLastVal]+sumDict[lastVal]
            count+=1
        return sumDict[n]   



if __name__=="__main__":
    num=25
    print(Solution().tribonacci(n=num))
