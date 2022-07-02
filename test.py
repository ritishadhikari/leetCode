from typing import List
from math import inf
class Solution:
     def maxProfit(self, prices):
          free = 0
          have = cool = float('-inf')
          for p in prices:
               free, have, cool = max(free, cool), max(have, free - p), have + p
          return max(free, cool)

if __name__=="__main__":
     prices=[5,2,3,0,2]
     print(Solution().maxProfit(prices=prices))
