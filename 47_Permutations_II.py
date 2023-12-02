from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # assign index to each elements
        numsElem=[[(n,i)] for i,n in enumerate(nums)]

        while len(numsElem[0])<len(nums):
            elementsAndValues=numsElem.pop(0)
            for i,v in enumerate(nums):
                if (v,i) not in (elementsAndValues):
                    numsElem.append(elementsAndValues+[(v,i)])
        
        # now only fetch the elements once
        getSet=set()
        for perm in numsElem:
            numList=[el for el,ind in perm]
            getSet.add(tuple(numList))
        return list(getSet)
                






if __name__=="__main__":
    nums=[1,1,2]
    print(Solution().permuteUnique(nums=nums))