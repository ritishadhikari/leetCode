import bisect
from typing import List
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        mod = 10**9 + 7
        absdiffsum, absdiff = 0, []
        mi = float('inf')
        n = len(nums1)
        for i in range(n):
            diff = abs(nums1[i] - nums2[i])
            absdiffsum += diff
            absdiff.append(diff)
        nums1.sort()
        for num, diff in zip(nums2, absdiff):
            idx = bisect.bisect_left(nums1, num)
            if idx > 0:
                mi = min(mi, absdiffsum - diff + abs(num - nums1[idx-1]))
            if idx < n:
                mi = min(mi, absdiffsum - diff + abs(num - nums1[idx]))
        return mi % mod


if __name__=="__main__":
    nums1 = [1,10,4,4,2,7]
    nums2 = [9,3,5,1,7,4]
    print(Solution().minAbsoluteSumDiff(nums1=nums1, nums2=nums2))