class Solution:
    def numDecodings(self, s: str) -> int:
        if s=="" or s[0]=="0":
            return 0
        else:
            dct={'futMultiplicationPossible':0,'futConcatenationPossible':1}
            for i in range(len(s)):
                tempVal=0
                if i and 10<=int(s[i-1:i+1])<=26:
                    tempVal=dct['futMultiplicationPossible']
                if int(s[i]):
                    tempVal+=dct['futConcatenationPossible']
                dct={'futMultiplicationPossible':dct['futConcatenationPossible'],
                'futConcatenationPossible':tempVal}
        
        return dct['futConcatenationPossible']

if __name__=="__main__":
    print(Solution().numDecodings(s='12'))