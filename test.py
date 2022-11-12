from collections import defaultdict, deque
from typing import List
import math
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, t: int) -> int:
        if not t: return 0
        
        threshold = max(forbidden + [t]) + a + b
        forbidden = set(forbidden)
        seen = set([0])
        q = [[0,0]]
        
        while q:
            pos, steps = q.pop(0)
            
            if pos+a not in forbidden and pos+a not in seen and pos+a <= threshold: 
                # Termination Condition
                if pos+a == t: return steps+1
                
                q.append([pos+a, steps+1])
                seen.add(pos+a)
                
            if pos-b > 0 and pos-b not in forbidden and pos-b not in seen: 
                # Termination Condition
                if pos-b == t: return steps+1
                seen.add(pos-b)
                
                if pos-b+a not in forbidden and pos-b+a not in seen and pos-b+a <= threshold:
                    # Termination Condition
                    if pos-b+a == t: return steps+2
                    
                    q.append([pos-b+a, steps+2])
                    seen.add(pos-b+a)
        return -1

if __name__=="__main__":
    if __name__=="__main__":
        forbidden = [128,178,147,165,63,11,150,20,158,144,136]  
        a=61
        b=170
        t=135
        print(Solution().minimumJumps(forbidden=forbidden,a=a,b=b,t=t))