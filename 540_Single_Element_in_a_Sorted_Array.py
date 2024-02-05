from typing import List
class Solution():
    '''
    the single number will always be at the even index
    # expectation is the even index and the subsequent odd index is same
    # if it is not same then the single number exists atleast prior to the middle number
    '''
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l=0
        h=len(nums)-1
        while l<=h:
            m=(l+h)//2
            # when we have actually arrived at the number with the single appearance
            if l==h: return nums[m]  
            #   odd condition                      even condition
            if (m%2==1 and nums[m]==nums[m-1]) or (m%2==0 and nums[m]==nums[m+1]):
                l=m+1
            else:
                # odd condition 
                if m%2==1:  h=m-1
                # even condition
                else: h=m
        return nums[m]


if __name__=="__main__":
    nums = [1,1,2,3,3,5,5]
    print(Solution().singleNonDuplicate(nums=nums))