from typing import List
from collections import Counter,defaultdict
class DetectSquares:

    def __init__(self):
        self.tracker=defaultdict(lambda: 0)
        

    def add(self, point: List[int]) -> None:
        self.tracker[tuple(point)]+=1
        

    def count(self, point: List[int]) -> int:
        count=0
        for ep in self.tracker.keys():
            # Presence of a potential diagonal
            if point[0]!=ep[0] and point[1]!=ep[1]:
                pp1=(point[0],ep[1])  # down/top
                pp2=(ep[0],point[1])  # left/right
                
                # Test for Square
                length,width=abs(point[0]-pp2[0]),abs(point[1]-pp1[1])
                condition=length==width
                # Presence of non diagonals in the array and 
                # satisfying square condition
                if pp1 in self.tracker and pp2 in self.tracker and condition:
                    count+=self.tracker[pp1]*self.tracker[pp2]*self.tracker[ep]
        return count
            


if __name__=="__main__":
    obj=DetectSquares()
    obj.add(point=[3,10])
    obj.add(point=[11,2])
    obj.add(point=[3,2])
    print(obj.count(point=[11,10]))
    print(obj.count(point=[14,8]))
    obj.add(point=[11,2])
    print(obj.count(point=[11,10]))

