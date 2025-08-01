from typing import List
from threading import Semaphore, Barrier

class H2O:
    def __init__(self):
        self.semH=Semaphore(value=2)
        self.semO=Semaphore(value=1)
        self.barrier=Barrier(parties=3)


    def hydrogen(self, releaseHydrogen: List[str]|None) -> None:
        with self.semH:
            self.barrier.wait()
            # releaseHydrogen() outputs "H". Do not change or remove this line.
            releaseHydrogen()


    def oxygen(self, releaseOxygen: List[str]|None) -> None:
        with self.semO:
            self.barrier.wait()
            
            # releaseOxygen() outputs "O". Do not change or remove this line.
            releaseOxygen()