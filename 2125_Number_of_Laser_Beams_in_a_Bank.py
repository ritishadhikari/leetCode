from typing import List
from collections import Counter

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total=0
        last=None
        for r in bank:
            ones=r.count("1")
            if last and ones:
                total+=last*ones
            if ones: 
                last=ones

        return total

if __name__=="__main__":
    bank=["000","111","000"]
    print(Solution().numberOfBeams(bank=bank))
        