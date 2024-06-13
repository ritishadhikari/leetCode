# VVI 
from typing import List
from collections import Counter
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        frequency=Counter(nums)
        answer=0
        for k,v in frequency.items():
            if target.startswith(k):
                suffix=target[len(k):]
                if suffix==k:
                    # if length of suffix and prefix are equal, the number of combinations 
                    # for a pattern with frequency n is n * (n-1), 
                    # which is written as n ^2 - n in the above code.
                    # For why its n * (n-1), all the each of the n spaces can be 
                    # filled/combined in n -1 ways with the other patterns.
                    answer+=(frequency[suffix]*(frequency[suffix]-1))
                else:
                    answer+=v*frequency[suffix]
        return answer
        


if __name__=="__main__":
    nums = ["777","7","77","77"]
    target="7777"
    print(Solution().numOfPairs(nums=nums, 
                                target=target))