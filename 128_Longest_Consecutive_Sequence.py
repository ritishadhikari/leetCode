from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count=0
        maxCount=0
        last=None
        last2Last=None
        for num in nums:
            if last==None:
                count+=1
                last=num
            else:
                if num-last==1:
                    count+=1
                    last2Last=last
                    last=num
                else:
                    if last2Last is None or num-last2Last==1:
                        last=num
                        continue
                    else:
                        maxCount=max(maxCount,count)
                        count=1
                        last2Last=None
                        last=num
        return max(maxCount,count)



if __name__=="__main__":
    nums = [4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3]
    print(Solution().longestConsecutive(nums=nums))