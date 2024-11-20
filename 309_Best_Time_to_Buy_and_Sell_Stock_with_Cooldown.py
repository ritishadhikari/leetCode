from typing import List
from math import inf
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cd,sell,hold=0,0,-inf
        for price in prices:
            last_cd,last_sell,last_hold=cd,sell,hold
            # This step remains unclear
            cd=max(last_cd,last_sell)
            # You can only sell the stock from your last hold price
            sell=last_hold+price
            # You can only decide to buy/hold the stock comparing one
            # previous day of cool down savings
            hold=max(last_hold,last_cd-price)
        return max(cd,sell)

if __name__=="__main__":
    prices = [1,2,3,0,2]
    print(Solution().maxProfit(prices=prices))