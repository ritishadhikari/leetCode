from typing import List
class Solution():
    '''
    the single number will always be at the even index
    '''
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l=0
        h=len(nums)-1
        while l<=h:
            m=(l+h)//2
            # additional check since we are dealing with the next or the prior index number
            if m==len(nums)-1: return nums[m]  
            #   odd condition                      even condition
            if (m%2==1 and nums[m]==nums[m-1]) or (m%2==0 and nums[m]==nums[m+1]):
                l=m+1
            else:
                if l==m==h or m%2==1:  h=m-1
                else: h=m
        return nums[m]


if __name__=="__main__":
    nums = [1]
    print(Solution().singleNonDuplicate(nums=nums))