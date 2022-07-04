from typing import List
class Solution:
    def generate(self,numRows:int) -> List[List[int]]:

        # array=[1]
        # finalArray=[array]
        # if numRows==1:
        #     return finalArray
        # else:
        #     for i in range(2,numRows+1):
        #         lastArray=array
        #         array=[]
        #         count=0
        #         while count<i:
        #             if count==0 or count==i-1:
        #                 toAdd=lastArray[0]
        #                 array.append(toAdd)
        #             else:
        #                 toAdd=lastArray[count-1]+lastArray[count]
        #                 array.append(toAdd)
        #             count+=1
        #         finalArray.append(array)
        # return finalArray

        finalArray=[[1]]

        for i in range(2,numRows+1):
            presentLatIndex=len(finalArray)-1
            newLatIndex=len(finalArray)
            finalArray.append([])
            count=0
            while count<i:
                if count==0 or count==i-1:
                    toAdd=finalArray[presentLatIndex][0]    
                else:
                    toAdd=finalArray[presentLatIndex][count-1]+finalArray[presentLatIndex][count]  
                finalArray[newLatIndex].append(toAdd)
                count+=1

        return finalArray

if __name__=="__main__":
    numRows=5
    print(Solution().generate(numRows=numRows))
