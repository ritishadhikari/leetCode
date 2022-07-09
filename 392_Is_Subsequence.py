class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointerAtS=0
        for l in t:
            if pointerAtS==len(s):
                break
            elif s[pointerAtS]==l:
                pointerAtS+=1
        return pointerAtS==len(s) 

if __name__=="__main__":
    s="aaaaaa"
    t="bbaaaa"
    print(Solution().isSubsequence(s=s,t=t))