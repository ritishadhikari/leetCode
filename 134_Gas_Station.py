# VVI
from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        else:
            start=0
            runningSum=0
            for i in range(len(gas)):
                runningSum=runningSum+gas[i]-cost[i]
                if runningSum<0:
                    start=i+1
                    runningSum=0
            return start

if __name__=="__main__":    
    gas = [7,1,0,11,4]
    cost = [5,9,1,2,5]
    print(Solution().canCompleteCircuit(gas=gas, cost=cost))