from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if total%2:
            return False
        else: 
            tot=total//2
            dp={i+1:False for i in range(tot)}
            getset=set()
            
            for i in nums:
                if i in dp:
                    dp[i]=True
                    getsett=set()
                    for n in getset:
                        if n+i in dp and not dp[n+i] :
                            dp[n+i]=True
                            # if n+i==tot:
                            #     return True
                            getsett.add(n+i)
                    getset.add(i)
                    for j in getsett: getset.add(j)
                    if dp[tot]: return dp[tot]

            return dp[tot]
if __name__=="__main__":
    nums=[8,4,5,2,7,1,3]
    print(Solution().canPartition(nums=nums))