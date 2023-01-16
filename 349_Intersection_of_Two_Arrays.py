from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        seen=set()
        nums2=sorted(nums2)

        def match(num):
            l=0
            r=len(nums2)-1
            while l<=r:
                m=(l+r)//2
                if nums2[m]>num: r=m-1
                elif nums2[m]<num:  l=m+1
                else: return True
            return False


        for el in nums1:
            if el not in seen:
                seen.add(el)
                if match(el): res.append(el)

        return res

if __name__=="__main__":
    nums1 = [4,9,5]
    nums2=[9,4,9,8,4]
    print(Solution().intersection(nums1=nums1, nums2=nums2))