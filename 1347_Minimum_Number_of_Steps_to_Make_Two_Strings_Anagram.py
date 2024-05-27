from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sDict=Counter(s)
        tDict=Counter(t)
        count=0
        for key,value in sDict.items():
            if key in tDict and value>tDict[key]:
                count+=value-tDict[key]
            elif key not in tDict:
                count+=value
        
        return count


if __name__=="__main__":
    s = "bab"
    t = "aba"
    print(Solution().minSteps(s=s,t=t))
        