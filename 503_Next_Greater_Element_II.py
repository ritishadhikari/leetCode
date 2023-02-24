from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        answer=[-1]*len(nums)
        
        for i,v in enumerate(nums):
            while stack and stack[-1][1]<v:
                index,_=stack.pop()
                answer[index]=v
            stack.append((i,v))
        
        for ri,rv in enumerate(nums):
            while stack and stack[-1][1]<rv:
                index,_=stack.pop()
                answer[index]=rv

        return answer

if __name__=="__main__":
    nums = [1,2,1]
    print(Solution().nextGreaterElements(nums=nums))