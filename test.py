from typing import List

class Solution:
  def PredictTheWinner(self, nums: List[int]) -> bool:
    arr = [0] * (n:= len(nums))

    for i in range(n-1,-1,-1):
        arr[i] = nums[i]
        
        for j in range(i+1, n):
            arr[j] = max(nums[i]-arr[j  ],
                            nums[j]-arr[j-1])
        
    return arr[n-1] >= 0    
  
if __name__=="__main__":
    nums=[1,5,233,6,9,4]
    print(Solution().PredictTheWinner(nums=nums))