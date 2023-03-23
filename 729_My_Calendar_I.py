class MyCalendar:

    def __init__(self):
        self.lst=[] 

    def book(self, start: int, end: int) -> bool:
        for s,e in self.lst:
            if start<e and end>s:
                return False
        self.lst.append((start,end))
        return True

if __name__=="__main__":
    obj = MyCalendar() 
    print(obj.book(start=48,end=50))
    print(obj.book(start=0,end=6))
    print(obj.book(start=6,end=14))
    print(obj.book(start=8,end=17))
    print(obj.book(start=15,end=23))
    print(obj.book(start=49,end=50))
    print(obj.book(start=45,end=50))
    print(obj.book(start=29,end=34))
    print(obj.book(start=3,end=12))
    print(obj.book(start=38,end=44))


    # print(obj.book(start=47,end=50))
    # print(obj.book(start=33,end=41))
    # print(obj.book(start=39,end=45))
    # print(obj.book(start=33,end=42))
    # print(obj.book(start=25,end=32))
    # print(obj.book(start=26,end=35))
    # print(obj.book(start=19,end=25))
    # print(obj.book(start=3,end=8))
    # print(obj.book(start=8,end=13))
    # print(obj.book(start=18,end=27))

