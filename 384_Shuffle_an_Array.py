from typing import List
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.arr=self.nums[:]
        
    def reset(self) -> List[int]:
        self.arr=self.nums[:]
        return self.arr

    def shuffle(self) -> List[int]:
        l=len(self.arr)
        for i in range(l-1,0,-1):
            targetIndex=random.randint(a=0,b=i)
            self.arr[i],self.arr[targetIndex]=self.arr[targetIndex],self.arr[i]
        return self.arr

if __name__=="__main__":
    array=[3, 1, 2]
    sol=Solution(nums=array)
    print(sol.shuffle())
    print(sol.reset())
    print(sol.shuffle())