import random
class RandomizedSet:

    def __init__(self):
        self.rSet=set()
        self.c=0

    def insert(self, val: int) -> bool:
        if val not in self.rSet:
            self.rSet.add(val)
            self.c+=1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.rSet:
            self.rSet.remove(val)
            self.c-=1
            return True
        else:
            return False

    def getRandom(self) -> int:
        randomNumber=int(random.uniform(a=0,b=self.c))
        return list(self.rSet)[randomNumber]

if __name__=="__main__":
    obj = RandomizedSet()
    print(obj.insert(val=1))
    print(obj.remove(val=2))
    print(obj.insert(val=2))
    print(obj.getRandom())
    print(obj.remove(val=1))
    print(obj.insert(val=2))
    print(obj.getRandom())