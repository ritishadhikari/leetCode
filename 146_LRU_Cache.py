from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.dct=OrderedDict()
        self.capacity=capacity

    def get(self, key: int) -> int:
        if key in self.dct:
            self.dct.move_to_end(key=key,last=True)
            return self.dct[key]
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.dct:
            self.dct.move_to_end(key=key,last=True)
        self.dct[key]=value
        if len(self.dct)>self.capacity:
            self.dct.pop(next(iter(self.dct)))

if __name__=="__main__":
    obj=LRUCache(capacity=2)
    print(obj.put(key=1,value=1))
    print(obj.put(key=2,value=2))
    print(obj.get(key=1))
    print(obj.put(key=3,value=3))
    print(obj.get(key=2))
    print(obj.put(key=4,value=4))
    print(obj.get(key=1))
    print(obj.get(key=3))
    print(obj.get(key=4))