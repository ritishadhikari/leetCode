from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
       
        low=0
        high=len(nums)-1
        answer=[0]*len(nums)

        while low<=high:
            if abs(nums[low])<abs(nums[high]):
                answer[high-low]=nums[high]**2
                high-=1
            else:
                answer[high-low]=nums[low]**2
                low+=1       
        return answer
    
       



if __name__=="__main__":
    numbers=[-7,-3,-2,-1,4,5,8]
    print(Solution().sortedSquares(nums=numbers))
    
