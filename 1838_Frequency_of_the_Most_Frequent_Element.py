# VVI
from typing import List
import bisect
class Solution:
    '''
    https://leetcode.com/problems/frequency-of-the-most-frequent-element/solutions/1179374/python-3-sliding-window-explanation-with-code/
    '''
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        best=1
        sumOfSeq=nums[0]
        i=0
        for j in range(1,len(nums)):
            sumOfSeq+=nums[j]
            while sumOfSeq+k<nums[j]*(j-i+1):
                sumOfSeq-=nums[i]
                i+=1  
            best=max(best,j-i+1)
        return best

if __name__=="__main__":
    # nums=[9922,9980,9990,9922,9932,9989,9929,9938,9941,9966,9985,9906,9964,9903,9995,9963,10000,9950,9939,9985,9944,9960,9989,9977,9901,9923,9997,9971,9909,9985,9979,9906,9955,9988,9996,9995,9901,9996,9924,9967,9991,9981,9914,9933,9946,9928,9975,9990,9968,9985,9963,9927,9946,9919,9931,9955,9979,9943,9905,9918,9962,9970,9939,9901,9940,9933,9917,9988,9935,9941,9947,9971,9901,9926,9908,9969,9978,9984,9952,9945,9958,9958,9930,9923,9950,9993,9938,9976,9942,9946,9990,9951,9971,9980,9966,9944,9976,9954,9970,9984,9939,9961,9996,9993,9935,9949,9975,9952,9998,9956,9957,9949,9902,9946,9979,9904,9925,9948,9952,9961,9948,9982,9922,9958,9956]
    # k=1911
    nums=[1,4,8,13]
    k=5
    # nums = [1,2,4]
    # k = 5
    print(Solution().maxFrequency(nums=nums,k=k))