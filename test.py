from bisect import bisect_left, bisect_right
from typing import List, Optional

class Solution:
		def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
			ans = []
			prefix = [0]
			for num in nums:
				prefix.append(prefix[-1]+num)
			
			n = len(prefix)
			for i in range(1,n):
				for j in range(i-1,-1,-1):
					total = prefix[i] - prefix[j]
					ans.append(total)
			
			ans.sort()
			return sum(ans[left-1:right])

if __name__=="__main__":

    nums = [1,2,3,4]
    n=4
    left=1
    right=5

    print(Solution().rangeSum(nums=nums,n=n, left=left,right=right))