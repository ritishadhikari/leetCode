from typing import List

class Solution:
    def search(self,nums:List[int], target:int):
        l=0
        r=len(nums)-1  # First Thing to keep note

        while(l<=r):  # Second Thing to keep note
            mid=(l+r)//2  # Third Thing to keep note
            if nums[mid]==target:
                return mid  # Fourth thing to keep note
            elif nums[mid]<target:
                l=mid+1  # Fifth thing to keep note
            else:
                r=mid-1  # Sixth thing to keep note
        return -1




if __name__=="__main__":
    nums=[-1,0,3,5,9,12,14]
    target=-4
    print(Solution().search(nums=nums, target=target))
