from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        '''
        purse={5:1,10:3,20:1}
        '''
        purse={}
        for denom in bills:
            if denom  not in purse:   purse[denom]=0
            purse[denom]+=1
            if denom==10:
                if 5 not in purse: return False
                else: 
                    purse[5]-=1
                    if purse[5]==0: purse.pop(5)
            elif denom==20:
                # if 10 found then one 10 and one 5
                if 10 in purse and 5 in purse:
                    purse[10]-=1
                    if purse[10]==0: purse.pop(10)
                    if purse[5]>=1:
                        purse[5]-=2
                        if purse[5]==0: purse.pop(5)
                    else: return False

                # if 10 not found then three 5
                elif 5 in purse and purse[5]>=3:
                    purse[5]-=3
                    if purse[5]==0: purse.pop(5)

                else: return False
        return True

if __name__=="__main__":
    bills = [5,5,10,10,20]
    print(Solution().lemonadeChange(bills=bills))