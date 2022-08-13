class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        # # solving s
        # S=''
        # for l in s:
        #     if l=="#":
        #         S=S[:-1]
        #     else:
        #         S+=l

        # # solving t
        # T=''
        # for l in t:
        #     if l=="#":
        #         T=T[:-1]
        #     else:
        #         T+=l
        
        # return False if S!=T else True

        maxLen=max(len(s),len(t))
        S=''
        T=''
        for i in range(maxLen):
            if i<len(s):
                if s[i]=="#":
                    S=S[:-1]
                else:
                    S+=s[i]
            if i<len(t):
                if t[i]=="#":
                    T=T[:-1]
                else:
                    T+=s[i]
        return False if S!=T else True

if __name__=="__main__":
    s="ab##"
    t="ad#c"
    print(Solution().backspaceCompare(s=s,t=t))