from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sDict=Counter(s)
        tDict=Counter(t)

        for key in tDict:
            if tDict[key]!=sDict[key]:
                return key

if __name__=="__main__":
    s = ""
    t = "y"
    print(Solution().findTheDifference(s=s,t=t))