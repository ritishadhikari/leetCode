from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
    #    left=0
    #    right=1
    #    while right<len(nums):
    #     if nums[left]==nums[right]:
    #         nums.pop(right)
    #     else:
    #         left+=1
    #         right+=1
        # Do not return anything as it is inplace

        seen=set()
        p=0
        length=len(nums)
        for i in range(length):
            if nums[i] not in seen:
                nums[p]=nums[i]
                seen.add(nums[i])
                p+=1
        # return nums

        for i in range(p,len(nums)):
            nums.pop()

        return nums
      


if __name__=="__main__":
    nums=[0,0,1,1,1,2,2,3,3,4]
    print(Solution().removeDuplicates(nums=nums))