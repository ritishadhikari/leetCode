# Can Skip
from typing import List
from math import inf

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        remaining=len(citations)
        for i,val in enumerate(citations):
            if remaining<=val:
                return remaining
            remaining-=1

        return 0


if __name__=="__main__":
    citations = [5,8,14,17,22,26]
    print(Solution().hIndex(citations=citations))