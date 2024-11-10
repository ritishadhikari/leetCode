from typing import Optional
from copy import deepcopy
import math
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        headC=head
        headIsForeign=False
        while head:
            if head.next and not headIsForeign:
                foreignVal=math.gcd(head.val,head.next.val)
                head.next=ListNode(val=foreignVal,
                                   next=head.next)
            head=head.next
            headIsForeign=False if headIsForeign else True
        return headC

if __name__=="__main__":
    head=ListNode(val=18,
                  next=ListNode(val=6,
                                next=ListNode(val=10,
                                              next=ListNode(val=3,
                                                            next=None))))
    print(Solution().insertGreatestCommonDivisors(head=head))