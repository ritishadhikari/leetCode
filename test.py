from typing import List
class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        current_min = nums[0] - k
        current_max = nums[-1] - k
        
        result = current_max - current_min
        
        if k == 0:
            return result
        
        end = len(nums) - 1
        for i in range(end):
            current_max = max(current_max, nums[i] + k)
            current_min = min(nums[0] + k, nums[i + 1] - k)
            result = min(result, current_max - current_min)
            
        return result
    
if __name__=="__main__":
    nums=[1,4,11,3,7]
    k=3
    print(Solution().smallestRangeII(nums=nums,k=k))