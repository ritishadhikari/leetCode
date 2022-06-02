from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ctr1 = Counter(s1)
        i = 0
        while i < len(s2) - len(s1) + 1:
            if s2[i] in ctr1:
                ctr2 = Counter(s2[i: i+len(s1)])
                if ctr1 == ctr2: 
                    return True
            i += 1
        return False

        ctr1=Counter(s1)
        i=0
        
        while i<=len(s2)-len(s1):
            if i not in ctr1:
                i+=1
            else:
                ctr2=Counter(s2[i:i+len(s1)])
                if ctr1==ctr2:
                    return True
        else:
            return False

if __name__=="__main__":
    print(Solution().checkInclusion(s1="ab", s2="eidboaoo"))