from typing import List
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff=abs(sum(aliceSizes)-sum(bobSizes))//2

        def match(size,arr):
            l=0
            r=len(arr)-1
            while l<=r:
                m=(l+r)//2
                if arr[m]<size:  l=m+1
                elif arr[m]>size:    r=m-1
                else: return True
            return False

        if sum(aliceSizes)<sum(bobSizes):
            bobSizes.sort()
            for i in aliceSizes:
                totalDiff=i+diff
                if match(size=totalDiff, arr=bobSizes): return [i,totalDiff]
        else:
            aliceSizes.sort()
            for i in bobSizes:
                totalDiff=i+diff
                if match(size=totalDiff, arr=aliceSizes): return [totalDiff,i]


if __name__=="__main__":
    aliceSizes = [20,35,22,6,13]
    bobSizes =[31,57]
    print(Solution().fairCandySwap(aliceSizes=aliceSizes,bobSizes=bobSizes))