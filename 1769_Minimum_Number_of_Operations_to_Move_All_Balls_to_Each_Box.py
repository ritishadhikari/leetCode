from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ones=[]
        for index,box in enumerate(boxes):
            if box=="1":
                ones.append(index)
        
        output=[]
        for index,box in enumerate(boxes):
            count=0
            for refIndex in ones:
                if index!=refIndex:
                    count+=abs(index-refIndex)
            output.append(count)
        return output


if __name__=="__main__":
    boxes="110"
    print(Solution().minOperations(boxes=boxes))