# VVI
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen=k+1
        freq=defaultdict(lambda: 0)
        for elem in s[:maxLen]:
            freq[elem]+=1
        leftPointer=0
        for i in range(maxLen,len(s)):
            freq[s[i]]+=1
            currLen=i+1-leftPointer
            if currLen-max(freq.values())<=k:
                maxLen=max(maxLen,currLen)
            else:
                freq[s[leftPointer]]-=1
                leftPointer+=1

        return maxLen

if __name__=="__main__":
    s="CABAAAABBBBBA"
    k=2
    print(Solution().characterReplacement(s=s,k=k))