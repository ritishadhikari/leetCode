from typing import List
class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        originalCapacity=capacity
        steps=0
        length=len(plants)
        for i in range(-1,length-1):
            fillingRequired=plants[i+1]
            remaining=capacity-fillingRequired
            if remaining>=0:
                capacity=remaining  # Exhaust
                steps+=1   # come to next
            else:
                steps+=(i+1)  # go back
                capacity=originalCapacity  # fill up
                steps+=(i+2)  # come to next
                capacity-=fillingRequired  # Exhaust
        return steps

if __name__=="__main__":
    plants = [3,2,4,2,1]
    capacity = 6
    print(Solution().wateringPlants(plants=plants,
                                    capacity=capacity))