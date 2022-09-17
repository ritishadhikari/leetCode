from typing import List
from collections import defaultdict, deque
from math import inf
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        if source==target:
            return 0
        stopBoard=defaultdict(lambda: [])
        for bus,route_bus in enumerate(routes):
            for route in route_bus:
                stopBoard[route].append(bus)
        stack=deque([source])
        busTaken=set()
        routeTaken=set()
        res=0
        while stack:
            res+=1
            lenStack=len(stack)
            for _ in range(lenStack):
                r=stack.popleft()
                routeTaken.add(r)
                for bus in stopBoard[r]:
                    if bus in busTaken: continue
                    else:
                        busTaken.add(bus)
                        for route in routes[bus]:
                            if route in routeTaken: continue
                            elif route==target: return res
                            else : stack.append(route)
        return -1
        
if __name__=="__main__":
 
    routes = [[1,2,7],[3,6,7],[9,2,8],[8,5,6]]
    source = 1
    target = 6
    print(Solution().numBusesToDestination(routes=routes,source=source,target=target))