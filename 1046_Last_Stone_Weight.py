from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stoneLoc=[[w,i] for i,w in enumerate(stones)]
        stoneLoc=sorted(stoneLoc,key=lambda k:k[0],reverse=True)
        
        while len(stoneLoc)>1:
            firstWeight,firstIndex=stoneLoc[0][0],stoneLoc[0][1]
            secondWeight,secondIndex=stoneLoc[1][0],stoneLoc[1][1]

            if firstWeight>secondWeight:
                stoneLoc[0][0]=firstWeight-secondWeight
                stoneLoc.remove([secondWeight,secondIndex])
            elif secondWeight>firstWeight:
                stoneLoc[1][0]=secondWeight-firstWeight
                stoneLoc.remove([firstWeight,firstIndex])
            else:
                stoneLoc.remove([firstWeight,firstIndex])
                stoneLoc.remove([secondWeight,secondIndex])
            stoneLoc=sorted(stoneLoc,key=lambda k:k[0],reverse=True)

            return 0 if not stoneLoc else stoneLoc[0][0]

if __name__=="__main__":
    stones = [2,2]
    print(Solution().lastStoneWeight(stones=stones))