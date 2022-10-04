class MyStack:

    def __init__(self):
        self.stack=[]
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def empty(self) -> bool:
        return False if self.stack else True

if __name__=="__main__":
    myStack=MyStack()
    myStack.push(x=1)
    myStack.push(x=2)
    myStack.top()
    myStack.pop()
    myStack.empty()
