from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l=0
        r=0
        mulVal=1
        count=0
        seen=-1
        while l<=r and r<len(nums):
            if r>seen:
                mulVal*=nums[r] 
                seen=r
            if mulVal>=k:
                count+=(r-l)
                mulVal//=nums[l]
                if l==r:   # for cases when another contagious series may begin 
                    r+=1 
                l+=1
            else:
                r+=1
        if r==len(nums):
            count+= ((r-l)*(r+1-l))//2
        return count

if __name__=="__main__":
    nums = [57,44,92,28,66,60,37,33,52,38,29,76,8,75,22]
    k = 18
    print(Solution().numSubarrayProductLessThanK(nums=nums,k=k))

