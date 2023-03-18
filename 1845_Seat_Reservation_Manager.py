import heapq
class SeatManager:
    
    def __init__(self,n:int):
        self.seat=[i for i in range(1,n+1)]
        heapq.heapify(self.seat)

    def reserve(self) -> int:
        return heapq.heappop(self.seat)        

    def unreserve(self,seatNumber: int) -> None:
        heapq.heappush(self.seat,seatNumber)

if __name__=="__main__":
    # obj=SeatManager(n=100)
    # print(obj.reserve())
    # print(obj.reserve())
    # print(obj.unreserve(1))
    # print(obj.unreserve(2))
    # print(obj.reserve())
    # print(obj.unreserve(1))
    # print(obj.reserve())
    # print(obj.unreserve(1))

    obj=SeatManager(n=100)
    print(obj.reserve())
    print(obj.reserve())
    print(obj.unreserve(2))
    print(obj.reserve())
    print(obj.reserve())
    print(obj.reserve())
    print(obj.reserve())
    print(obj.unreserve(5))

    # print(obj.seat)

