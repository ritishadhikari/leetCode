# Can Skip
from typing import List
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        for i in range(len(pref)-1,0,-1):
            pref[i]^=pref[i-1]
        return pref


if __name__=="__main__":
    pref=[13]
    print(Solution().findArray(pref=pref))
        