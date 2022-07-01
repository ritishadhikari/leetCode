from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        totalProfit=0
        lastBuy=0

        for index, price in enumerate(prices):
            if index:
                profit=max(0,price-lastBuy)
                totalProfit=profit+totalProfit
            lastBuy=price
        
        return totalProfit

if __name__=="__main__":
    prices=[7,6,4,3,1]
    print(Solution().maxProfit(prices=prices))