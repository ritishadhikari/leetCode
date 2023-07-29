import heapq
from math import inf
class SmallestInfiniteSet:
    def __init__(self):
        self.lst=[int(i) for i in range(1,1001)]
        self.tracker=set(self.lst)
        heapq.heapify(self.lst)
        

    def popSmallest(self) -> int:
        num=heapq.heappop(self.lst)
        self.tracker.remove(num)
        return num

    def addBack(self, num:int):
        if num not in self.tracker:
            heapq.heappush(self.lst,num)
            self.tracker.add(num)


if __name__=="__main__":
    obj=SmallestInfiniteSet()
    obj.addBack(num=2)
    print(obj.popSmallest())
    print(obj.popSmallest())
    print(obj.popSmallest())
    obj.addBack(num=1)
    print(obj.popSmallest())
    print(obj.popSmallest())
    print(obj.popSmallest())

