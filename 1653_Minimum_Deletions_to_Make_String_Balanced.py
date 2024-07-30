class Solution:
    def minimumDeletions(self, s: str) -> int:
       # Cost is incurred only when you see a after b
        bRemovalCost=0
        currentCost=0
        for ch in s:
            if ch == 'b':
                bRemovalCost+=1
            else:
                currentCost=min(currentCost+1,bRemovalCost)
    
        return currentCost

if __name__=="__main__":
    s="aababbab"
    print(Solution().minimumDeletions(s=s))