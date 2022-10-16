class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        traceDict={}
        a=0
        for i in range(48,58):
            traceDict[i]=a
            a+=1
    
        num=0
        multiplier=10
        for i in num1:
            num=traceDict[ord(i)]+num*multiplier
        num1=num

        num=0
        multiplier=10
        for i in num2:
            num=traceDict[ord(i)]+num*multiplier
        num2=num

        return str(num1+num2)

if __name__=="__main__":
    num1 = "456"
    num2 = "77"
    print(Solution().addStrings(num1=num1,num2=num2))