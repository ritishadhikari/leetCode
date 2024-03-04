from typing import List
from math import inf
class Solution:
    '''
        ref: https://leetcode.com/problems/kth-missing-positive-number/solutions/1004535/python-two-solutions-o-n-and-o-log-n-explained/?orderBy=most_votes
    '''
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l=0
        r=len(arr)-1
        inside=False
        M=r
        D=inf
        while l<=r:
            m=(l+r)//2
            diff=arr[m]-(m+1)
            if diff>=k:
                inside=True
                M=min(M,m)
                r=m-1
                D=min(D,diff)
            else:
                l=m+1
        return arr[M]-(D-k+1) if inside else arr[M]+(k-diff)
    
if __name__=="__main__":
    arr = [1,14,21,22,25]
    k=12
    print(Solution().findKthPositive(arr=arr,k=k))