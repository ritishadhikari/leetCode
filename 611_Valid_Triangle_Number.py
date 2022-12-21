from typing import List
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        nums=sorted(nums)
        for i in range(2,n):
            l=0
            r=i-1
            while l<r:
                if nums[l]+nums[r]>nums[i]:
                    count+=(r-l)
                    r-=1
                else:
                    l+=1
        return count


if __name__=="__main__":
    nums = [2,2,4,3,3]
    print(Solution().triangleNumber(nums=nums))
    '''
    nums = [2,2,4,3,3]
    nums = [2,2,3,3,4]
    2[0],2[1],3[2]
    2[0],3[2],3[3]
    2[1],3[2],3[3]
    2[0],2[1],3[3]
    2[0],3[3],4[4]
    2[1],3[3],4[4]
    3[2],3[3],4[4]
    2[0],3[2],4[4]
    2[1],3[2],4[4]
    
    '''
