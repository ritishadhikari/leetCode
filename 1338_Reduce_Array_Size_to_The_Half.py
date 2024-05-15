from typing import List
from collections import Counter
from math import inf
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        totalElem=len(arr)
        arr=sorted(Counter(arr).values(),reverse=True)
        best=inf
        def exceedingHalf(position):
            total=0
            for i in range(position):
                total+=arr[i]
                if total>=totalElem/2:
                    return True
            return False

        l,r=0,len(arr)
        while l<=r:
            m=(l+r)//2
            if exceedingHalf(position=m):
                best=min(best,m)
                r=m-1
            else:
                l=m+1
        return best

if __name__=="__main__":
    arr = [7,7,7,7,7,7]
    print(Solution().minSetSize(arr=arr))