from typing import List
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q=[start]
        seen=set()
        while q:
            start=q.pop()
            if start not in seen:
                seen.add(start)
                backIndex=start-arr[start]
                forwardIndex=start+arr[start]
                if backIndex>=0:
                    if arr[backIndex]==0:	return True
                    else:	q.append(backIndex)
                if forwardIndex<=len(arr)-1:
                    if arr[forwardIndex]==0:	return True
                    else: q.append(forwardIndex)
        return False
        

if __name__=='__main__':
    arr=[4,2,3,0,3,1,2]
    start=5
    print(Solution().canReach(arr=arr,start=start))