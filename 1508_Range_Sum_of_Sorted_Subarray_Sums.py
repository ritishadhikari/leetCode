from typing import List
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        cumSum=[]
        for i in nums:
            if len(cumSum)==0:cumSum.append(i)
            else: cumSum.append(cumSum[-1]+i)
        
        ans=[]
        for i in range(len(cumSum)):
            ans.append(cumSum[i])
            for j in range(i-1,-1,-1):
                ans.append(cumSum[i]-cumSum[j])
        ans.sort()
        return sum(ans[left-1:right])%(10**9+7)

        # This will also work
        ans=[]
        for i in range(n):
            last=nums[i]
            ans.append(last)
            for j in range(i+1,n):
                last=last+nums[j]
                ans.append(last)
        return sum(sorted(ans)[left-1:right])%(10**9+7)

if __name__=="__main__":
    nums=[3,5,7,8,9]
    n=len(nums)
    left=3
    right=5
    print(Solution().rangeSum(nums=nums,n=n,left=left,right=right))