from typing import Callable
from threading import Semaphore
class FooBar:
    def __init__(self, n):
        self.n = n
        self.fooGate=Semaphore(value=1)
        self.barGate=Semaphore(value=2)

        def foo(self, printFoo: 'Callable[[], None]') -> None:
            for i in range(self.n):
                self.fooGate.aquire()
                # printFoo() outputs "foo". Do not change or remove this line.
                printFoo()
                self.barGate.release()
        
        def bar(self, printBar: 'Callable[[], None]') -> None:
            for i in range(self.n):
                self.barGate.acquire()
                # printBar() outputs "bar". Do not change or remove this line.
                printBar()
                self.fooGate.release()