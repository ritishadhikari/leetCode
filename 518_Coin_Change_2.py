# VIP
from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[1]+[0 for i in range(amount)]

        for i in coins:
            for j in range(i,len(dp)):
                dp[j]=dp[j]+dp[j-i]

        return dp[amount]

if __name__=="__main__":
    amount = 16
    coins = [2,5,3]
    print(Solution().change(amount=amount,coins=coins))