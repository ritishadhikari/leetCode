from typing import List
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        nums= int(''.join([str(f) for f in num]))+k

        return [int(s) for s in str(nums)]
    
    


if __name__=="__main__":
    num = [1,2,0,0]
    num=[9,9,9]
    k = 1021
    print(Solution().addToArrayForm(num=num,k=k))