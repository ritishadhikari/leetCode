from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tracker={}
        for n in nums:
            if n not in tracker:
                tracker[n]=0
            tracker[n]+=1

        return sorted([(key,value) for key,value in tracker.items()],key=lambda k: k[1])[0][0]
            

if __name__=="__main__":
    nums=[0,1,0,1,0,1,99]
    print(Solution().singleNumber(nums=nums))