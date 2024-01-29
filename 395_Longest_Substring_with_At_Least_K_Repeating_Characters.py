# VVI
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
    
        uniqueChars=set(s)
        totalChars=len(s)
        res=0

        for charNo in range(1,len(uniqueChars)+1):
            i=0
            j=0
            tracker={}

            while j<totalChars:
                if s[j] not in tracker:
                    tracker[s[j]]=1
                else:
                    tracker[s[j]]+=1
        
                if len(tracker)<charNo:
                    j+=1
                    continue
                elif len(tracker)==charNo:
                    count=0
                    for key,value in tracker.items():
                        if value>=k:
                            count+=1
                            if count==charNo:
                                res=max(res,j-i+1)
                else:
                        while len(tracker)>charNo:
                            tracker[s[i]]-=1
                            if tracker[s[i]]==0:
                                tracker.pop(s[i])
                            i+=1

                j+=1

        return res

if __name__=="__main__":
    s = "bchhbbdefghiaaacb"
    k=3
    s='ababbc'
    k=2
    print(Solution().longestSubstring(s=s,k=k))