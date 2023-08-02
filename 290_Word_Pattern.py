class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p=[pat for pat in pattern]
        ss=s.split(" ")
        if len(p)!=len(ss):
            return False

        tracker={}
        tracker1={}

        for i,l in enumerate(p):
            if l not in tracker and ss[i] not in tracker1:
                tracker[l]=ss[i]
                tracker1[ss[i]]=l
            elif l in tracker:
                if tracker[l]!=ss[i]:
                    return False
            elif ss[i] in tracker1:
                if tracker1[ss[i]]!=l:
                    return False
        
        return True



if __name__=="__main__":
    pattern="abba"
    s="dog dog dog dog"
    print(Solution().wordPattern(pattern=pattern, s=s))