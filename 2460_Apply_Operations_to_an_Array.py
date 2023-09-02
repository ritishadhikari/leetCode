from typing import List
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        tracker=[]
        length=len(nums)

        cw=nums[0]
        for i in range(length):
            if i==length-1:
                if cw!=0:
                    tracker.append(cw)
            else:
                if cw==nums[i+1]:
                    if cw!=0:
                        tracker.append(cw*2)
                    cw=0
                else:
                    if cw!=0:
                        tracker.append(cw)
                    cw=nums[i+1]

        shortfall=length-len(tracker)
        tracker.extend([0]*shortfall)
        return tracker

if __name__=="__main__":
    nums = [0,0,0]
    print(Solution().applyOperations(nums=nums))