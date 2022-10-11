from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        first=None
        res=[]
        for val in nums:
            if first is None:
                first=int(val)
            else:
                if val-1>last:
                    res.append(f"{first}") if first==last else res.append(f"{first}->{last}")
                    first=int(val)
            last=int(val)
        if first is not None:  # This means the input array was not null
            res.append(f"{first}") if first==last else res.append(f"{first}->{last}")
        return res
if __name__=="__main__":
    nums = []
    print(Solution().summaryRanges(nums=nums))