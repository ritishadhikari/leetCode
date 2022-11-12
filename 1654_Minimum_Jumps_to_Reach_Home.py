from typing import List
from collections import deque
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        if x==0: return 0
        threshold=max(forbidden+[x])+a+b
        seen=set([0])
        forbidden=set(forbidden)
        q=[(0,0)]

        while q:
            pos,steps=q.pop(0)

            #Go Forward
            if pos+a<=threshold and pos+a not in seen and pos+a not in forbidden:
                if pos+a==x:
                    return steps+1
                seen.add(pos+a)
                q.append((pos+a,steps+1))
            if pos-b>=0 and pos-b not in seen and pos-b not in forbidden:
                if pos-b==x:
                    return steps+1
                seen.add(pos-b)
                if pos-b+a<=threshold and pos-b+a not in seen and pos-b+a not in forbidden:
                    if pos-b+a==x: return steps+2
                    seen.add(pos-b+a)
                    q.append((pos-b+a,steps+2))
        return -1
                

if __name__=="__main__":
    forbidden = [128,178,147,165,63,11,150,20,158,144,136]  
    a=61
    b=170
    x=135
    print(Solution().minimumJumps(forbidden=forbidden,a=a,b=b,x=x))


'''
61->122->183->13->74->135

'''