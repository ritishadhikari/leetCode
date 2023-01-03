from typing import List
class Solution:
     def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        l=0
        r=len(removable)
        best=l

        def output(guess):
            numbers=set(removable[:guess])
            f=""
            for i,str in enumerate(s):
                if i not in numbers:
                    f+=str
            return f
        
        def isSubsequence(trimmedString):
            refIndex=0
            for i,str in enumerate(trimmedString):
                if str==p[refIndex]:    refIndex+=1
                if refIndex==len(p): return True
                if len(p)-refIndex+1>len(trimmedString)-i+1: return False
            return False
            
        while l<=r:
            m=(l+r)//2
            trimmedString=output(guess=m)
            if isSubsequence(trimmedString=trimmedString):
                best=max(best,m)
                l=m+1
            else:
                r=m-1
                
        return best
                

if __name__=="__main__":
    s = "abcab"
    p = "abc"
    removable = [0,1,2,3,4]
    print(Solution().maximumRemovals(s=s,p=p,removable=removable))