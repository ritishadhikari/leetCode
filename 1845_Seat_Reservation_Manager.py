import heapq
class SeatManager:
    
    def __init__(self,n:int):
        self.seat=[i for i in range(1,n+1)]
        self.unreservedSeat=set(self.seat)
        heapq.heapify(self.seat)

    def reserve(self) -> int:
        seatToReserve=heapq.heappop(self.seat)   
        self.unreservedSeat.remove(seatToReserve)
        return seatToReserve     

    def unreserve(self,seatNumber: int) -> None:
        if seatNumber not in self.unreservedSeat:
            heapq.heappush(self.seat,seatNumber)
            self.unreservedSeat.add(seatNumber)

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
    print(obj.unreserve(3))
    print(obj.reserve())
    print(obj.reserve())
    print(obj.reserve())
    print(obj.reserve())
    print(obj.unreserve(5))

    # print(obj.seat)

