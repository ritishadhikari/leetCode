# VVI
from typing import List
from collections import defaultdict
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward=defaultdict(lambda:1)
        back=defaultdict(lambda:1)
        fm,bm=1,1
        for i in range(len(nums)):
            b=(i*-1)-1
            fm*=nums[i]
            bm*=nums[b]
            forward[i],back[b]=fm,bm
        answer=[]
        for i in range(len(nums)):
            fmi,bmi=i-1,(len(nums)*-1)+i+1
            answer.append(forward[fmi]*back[bmi])
        return answer
        
        
        
        answer=[1]*len(nums)
        suffix=1
        prefix=1

        for i in range(len(nums)):
            answer[i]*=prefix
            prefix*=nums[i]
            answer[-1-i]*=suffix
            suffix*=nums[-1-i]

        return answer


if __name__=="__main__":
    nums = [2,8,5,5,4]
    print(Solution().productExceptSelf(nums=nums))