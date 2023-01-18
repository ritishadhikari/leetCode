from typing import List
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        l=0
        r=len(nums)
        best=-1

        '''
        guess>count, reduce guess
        guess==count, increase guess
        guess<count, increase guess
        '''
        def valid(guess):
            count=0
            for n in nums:
                if n>=guess:    count+=1
            if guess==count: return "match"
            elif guess<count: return "increment"
            else: return "decrement"

        while l<=r:
            m=(l+r)//2
            if valid(m)=='match':
                best=max(m,best)
                l=m+1
            elif valid(m)=="increment":
                l=m+1
            if valid(m)=="decrement": 
                r=m-1
            
        return best

if __name__=="__main__":
    nums=[0,0]
    print(Solution().specialArray(nums=nums))