class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        evalDictS={}
        evalDictT={}

        for index,sString in enumerate(s):
            tString=t[index]

            # S
            if sString not in evalDictS:
                evalDictS[sString]=tString
            elif evalDictS[sString]!=tString:
                return False
            
            # T
            if tString not in evalDictT:
                evalDictT[tString]=sString
            elif evalDictT[tString]!=sString:
                return False
        return True
            
if __name__=="__main__":
    s="paper"
    t="title"
    print(Solution().isIsomorphic(s=s,t=t))