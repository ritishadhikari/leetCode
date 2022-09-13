from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if total%2:
            return False
        else: 
            tot=total//2
            dct={i+1:False for i in range(tot)}
            getset=set()
            
            for i in nums:
                if i in dct:
                    dct[i]=True
                    getsett=set()
                    for n in getset:
                        if n+i in dct:
                            dct[n+i]=True
                            getsett.add(n+i)
                    getset.add(i)
                    for j in getsett:
                        getset.add(j)
            return dct[tot]
if __name__=="__main__":
    nums=[3,3,3,4,5]
    print(Solution().canPartition(nums=nums))