from typing import List

class Solution():
    def chalkReplacer(self, chalk:List[int],k:int) -> int:
        s=sum(chalk)
        k=k%s
        for i,c in enumerate(chalk):
            if c>k: return i
            else: k=k-c

if __name__=="__main__":
    chalk=[5,1,5]
    k=7
    print(Solution().chalkReplacer(chalk=chalk, k=k))