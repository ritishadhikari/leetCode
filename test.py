from bisect import bisect_left, bisect_right
from typing import List, Optional

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1]+num)
        # prefix[i] <= prefix[j]-prefix[i] <= prefix[-1]-prefix[j]
        # => prefix[i]*2 <= prefix[j] <= (prefix[-1]+prefix[i])/2
        # find the range of j: lower <= j < upper
        ways = 0
        for i in range(1, len(prefix)-2):
            # lower = lower bound of j
            lower = bisect_left(prefix, prefix[i]*2) # prefix[i]*2 <= prefix[j]
            # upper = (upper bound of j) + 1
            upper = bisect_right(prefix, (prefix[-1]+prefix[i])/2) # prefix[j] <= (prefix[-1]+prefix[i])/2
            # i+1 <= lower < upper <= len(prefix)-1
            ways += max(0, min(upper, len(prefix)-1) - max(lower, i+1))
        return ways % (10**9+7)

if __name__=="__main__":

    nums = [1,2,2,2,5,0]

    print(Solution().waysToSplit(nums=nums))