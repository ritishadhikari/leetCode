from typing import List
from math import inf
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: 'int') -> 'int':
        evalList=[0]+ [inf for i in range(amount)]
        for i in range(1,len(evalList)):
            for coin in coins:
                if i>=coin:
                    evalList[i]=min(evalList[i],evalList[i-coin]+1)
        if evalList[-1]==inf:
            return -1
        else:
            return evalList[-1]
if __name__=="__main__":
    coins = [5,3]
    amount = 15
    print(Solution().coinChange(coins=coins,amount=amount))