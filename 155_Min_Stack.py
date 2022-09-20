from collections import deque
from math import inf
class MinStack:

    def __init__(self) -> None:
        self.obj=deque()

    def push(self, val:int) -> None:
        if not len(self.obj):
            self.minVal=val
        else:
            self.minVal=min(self.obj[-1][1],val)
        self.obj.append((val,self.minVal))
       
    def pop(self) -> None:
        self.obj.pop()[0]

    def top(self) -> int:
        return self.obj[-1][0]

    def getMin(self) -> int:
        return self.obj[-1][1]

if __name__=="__main__":
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())  # -3
    obj.pop()
    print(obj.top())  # 0
    print(obj.getMin())
