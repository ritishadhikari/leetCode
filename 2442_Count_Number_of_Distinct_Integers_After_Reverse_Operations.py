from typing import List
class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        length=len(nums)
        initialNums=set(nums)
        for i in range(length):
            num=int(str(nums[i])[::-1])
            print(num)
            if num not in initialNums:
                nums.append(num)
        return len(set(nums))

if __name__=="__main__":
    nums=[1,13,10,12,31]
    print(Solution().countDistinctIntegers(nums=nums))