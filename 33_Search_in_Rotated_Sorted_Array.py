from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length=len(nums)
        l=0
        r=length-1
        m=(r+l)//2
        while l<=r:
            sl=True if nums[l]<=nums[m] else False  # Whether Left from mid is sorted
            sr=True if nums[r]>=nums[m] else False  # Whether right from d mis sorted
            if target==nums[m]:
                return m
            else:
                if target>nums[m]:
                    if sl and sr or sl and not sr:  # When Number is part of unsorted right from mid
                        l=m+1
                        m=(r+l)//2
                    elif not sl and sr:
                        if nums[r]>=target:  # When Number is/may part of sorted right from mid
                            l=m+1
                            m=(r+l)//2
                        else:  # When Number is/may part of unsorted Left from Mid
                            r=m-1
                            m=(r+l)//2
                else:
                    if sl and sr or sr and not sl:  # When Number is part of unsorted left from mid
                        r=m-1
                        m=(r+l)//2
                    elif not sr and sl:
                        if nums[l]<=target:  # When Number is/may part of sorted left from mid
                            r=m-1
                            m=(r+l)//2
                        else:   # When Number is/may part of unsorted right from Mid
                            l=m+1
                            m=(r+l)//2
        return -1    


if __name__=="__main__":
    nums = [1]
    target=0
    print(Solution().search(nums=nums,target=target))