from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp=[1]+[0 for i in range(target)]
        for i in range(1, len(dp)):
            for j in nums:
                if i>=j:
                    dp[i]=dp[i]+dp[i-j]
        return dp[-1]


if __name__=="__main__":
    nums = [1,2,3]
    target = 4
    print(Solution().combinationSum4(nums=nums, target=target))