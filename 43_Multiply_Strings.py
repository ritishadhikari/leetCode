class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        # # First Number
        # n1=0
        # mf=1
        # for ch in num1[::-1]:
        #     n1 += (ord(ch)-48)*mf
        #     mf*=10

        # # Second Number
        # n2=0
        # mf=1
        # for ch in num2[::-1]:
        #     n2 += (ord(ch)-48)*mf
        #     mf*=10

        # return str(n1*n2)

        maxLen=max(len(num1),len(num2))

        n1,n2=0,0
        mf1,mf2=1,1
        for i in range(maxLen):

            # First Number
            if i<len(num1):
                n1 += (ord(num1[-i-1])-48)*mf1
                mf1*=10

             # Second Number
            if i<len(num2):
                n2 += (ord(num2[-i-1])-48)*mf2
                mf2*=10
        return str(n1*n2)

if __name__=="__main__":
    num1 = "2" 
    num2 = "3"
    print(Solution().multiply(num1=num1,num2=num2))