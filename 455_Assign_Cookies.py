from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i,j=0,0
        res=0
        while i<len(g) and j<len(s):
            if s[j]>=g[i]:
                i+=1
                res+=1
            j+=1
        return res


if __name__=="__main__":
    g = [10,9,8,7]
    s = [5,6,7,8]
    print(Solution().findContentChildren(g=g,s=s))