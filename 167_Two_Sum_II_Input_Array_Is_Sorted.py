from typing import List
class Solution:
    def twoSum(self, numbers:List[int], target:int) -> List[int]:
        # dct={}  # using a dictionary

        # for index,element in enumerate(numbers):
        #     if element not in dct:
        #         dct[target-element]=index+1
        #     elif element in dct:
        #         return [dct[element],index+1]   #using a list

        ## Alternate

        l,r=0,len(numbers)-1  # Two Additional Variables

        while l<=r:
            if numbers[l]+numbers[r]==target:
                return [l+1,r+1]
            elif numbers[l]+numbers[r]<target:
                l+=1
            elif numbers[l]+numbers[r]>target:
                r-=1

if __name__=="__main__":
    numbers = [2,7,11,15]
    target = 9

    print(Solution().twoSum(numbers=numbers,target=target))
