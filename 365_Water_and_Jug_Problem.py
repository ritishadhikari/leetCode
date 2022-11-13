import math,fractions
class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if targetCapacity==0:return True
        elif jug1Capacity+jug2Capacity<targetCapacity:return False
        else:
            gcd=math.gcd(jug1Capacity,jug2Capacity)
            return True if targetCapacity%gcd==0 else False



if __name__=="__main__":
    jug1Capacity = 3
    jug2Capacity = 5
    targetCapacity = 4
    print(Solution().canMeasureWater(jug1Capacity=jug1Capacity,jug2Capacity=jug2Capacity,targetCapacity=targetCapacity))