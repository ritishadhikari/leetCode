
class LinkedList:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next


class MyCircularQueue:

    def __init__(self, k: int):
        self.max=k
        self.size=0
        self.head=None
        self.tail=None
        
    def enQueue(self, value: int) -> bool:
        if self.isFull(): 
            return False
        else:
            if self.isEmpty():
                self.head=self.tail=LinkedList(val=value)
            else:
                self.tail.next=LinkedList(val=value)
                self.tail=self.tail.next
            self.size+=1
            return True
        
    def deQueue(self) -> bool:
        if self.isEmpty(): 
            return False
        else:
            self.head=self.head.next
            self.size-=1
            return True
        
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.head.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.tail.val

    def isEmpty(self) -> bool:
        if self.size==0: return True
        else: return False

    def isFull(self) -> bool:
        if self.size==self.max: return True
        else: return False

if __name__=="__main__":
    obj = MyCircularQueue(k=3)
    print(obj.enQueue(value=1))
    print(obj.enQueue(value=2))
    print(obj.enQueue(value=3))
    print(obj.enQueue(value=4))
    print(obj.Rear())
    print(obj.isFull())
    print(obj.deQueue())
    print(obj.enQueue(value=4))
    print(obj.Rear())

    