from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        digits=int("".join(str(i) for i in digits))

        return [int(s) for s in str(digits+1)]

       
            

if __name__=="__main__":
    digits=[1,2,3]
    print(Solution().plusOne(digits=digits))