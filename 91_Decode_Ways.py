class Solution:
    def numDecodings(self, s: str) -> int:
        if s=="" or s[0]=="0":
            return 0
        else:
            dct={'multiplyLastTwoVals':0,'concatenate':1}
            for i in range(len(s)):
                tempVal=0
                if int(s[i]):
                    tempVal=dct['concatenate']
                if i and 10<=int(s[i-1:i+1])<=26:
                    tempVal+=dct['multiplyLastTwoVals']
                dct={'multiplyLastTwoVals':dct['concatenate'],'concatenate':tempVal}
        
        return dct['concatenate']

if __name__=="__main__":
    print(Solution().numDecodings(s='10'))