from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[[]]
        for n in nums:
            for i in range(len(result)):
                result.append(result[i]+[n])
        return result

if __name__=="__main__":
    nums = [1,2,3]
    print(Solution().subsets(nums=nums))