from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        array=[1]
        if rowIndex==0:
            return array[0]
        else:
            for i in range(1,rowIndex+1):
                preArray=array
                array=[]
                for j in range(i+1):
                    if not j or j==i:
                        array.append(1)
                    else:
                        array.append(preArray[j] + preArray[j-1])
            return array
if __name__=="__main__":
    rowIndex=5
    print(Solution().getRow(rowIndex=rowIndex))