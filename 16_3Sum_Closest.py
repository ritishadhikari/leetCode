# VVI

# Adjust s to get the most optimum res

from typing import List, Dict
from collections import defaultdict

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res=sum(nums[:3])
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                s=sum((nums[i],nums[l],nums[r]))
                if abs(s-target)<abs(res-target):
                    res=s
                if s>target:
                    r-=1
                elif s<target:
                    l+=1
                else:
                    return s
        return s

if __name__=="__main__":
    # nums=[-300,-255,194,-977,-280,-878,832,755,23,466,-773,239,140,27,-627,170,275,-840,307,-22,-520,954,576,960,-997,-707,718,-433,771,371,467,473,204,-392,-842,-886,44,-681,12,573,240,442,604,821,-171,-173,394,247,761,-474,-10,985,349,482,-640,701,303,-744,295,-373,113,471,-785,-855,575,-3,890,-9,379,-87,959,942,997,-434,-145,825,618,919,-837,775,-588,75,-895,121,-567,913,-41,787,292,210,61,-12,-918,696,-338,-15,-606,65,529,107,773,-221,896,556,280,512,-298,647,-725,34,-57,-685,-829,-479,-355,-802,-55,659,860,554,-217,187,450,776,-413,-618,-116,626,324,753,697,150,822,-585,-608,391,-322,348,386,861,-470,-883,-521,-324,-616,829,720,262,-723,-871,-996,-805,624,237,182,798,251,616,909,-468,751,-194,731,-234,835,-974,498,-544,-113,873,256,-751,318,-575,-793,-351,329,759,-948,714,-589,-385,-135,118,-94,723,-812,97,486,-889,-24,-312,-100,972,462,-759,242,142,-732,-961,-391,607,-984,558,-162,143,368,595,-224,-346,-966,264,-528,87,255,-506,-398,-429,-67,772,-662,478,-327,370,623,-690,67,-161,-669,268,-139,797,597,726,801,-361,-701,-214,844,-857,-127,296,98,-165,-620,-591,91,-99,-426,-339,421,-456,-181,-825,878,-940,783,449,-39,-991,504,961,-927,6,186,-949,-963,361,740,402,-177,-693,536,523,-867,808,173,30,-503,665,26,480,657,-269,422,747,-274,-198,334,71,311,-815,176,-652,-1,-632,241,248,245,429,46,-370,887,185,-461,-90,-383,958,792,-299,-658,933]
    # nums=[-1,2,1,-4]
    nums=[4,0,5,-5,3,3,0,-4,-5]
    target=-2
    print(Solution().threeSumClosest(nums=nums, target=target))