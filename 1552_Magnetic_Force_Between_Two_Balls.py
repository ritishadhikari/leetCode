from typing import List
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        position.sort()
        def valid(guess):
            ans=1
            cur=position[0]
            for p in position:
                if p-cur>=guess:
                    cur=p
                    ans+=1
                    if ans>=m: return True
            return False
        l=0
        r=position[-1]-position[0]
        best=l
        while l<=r:
            mid=(r+l)//2
            if valid(guess=mid):
                best=max(best,mid)
                l=mid+1
            else:
                r=mid-1
        return best

if __name__=="__main__":
    position=[5,4,3,2,1,1000000000]
    m=2
    print(Solution().maxDistance(position=position, m=m))
