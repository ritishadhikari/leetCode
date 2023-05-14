from typing import List
from math import inf
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        if len(list1)<len(list2):
            consider=list1
            reference=list2
        else:
            consider=list2
            reference=list1
        
        ans=[]
        minIndex=inf
        for index, val in enumerate(consider):
            if val in set(reference):
                refIndex=reference.index(val)
                if index+refIndex<=minIndex:
                    if index+refIndex<minIndex:
                        ans=[]
                    minIndex=index+refIndex
                    ans.append(val)
               
        return ans

if __name__=="__main__":
    list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
    list2 = ["KFC","Shogun","Burger King"]
    print(Solution().findRestaurant(list1=list1, list2=list2))