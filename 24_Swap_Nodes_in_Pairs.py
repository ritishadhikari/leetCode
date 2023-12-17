from typing import List,Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        headC=head
        seen=set()
        while headC:
            if headC not in seen:
                if headC.next:
                    headC.val,headC.next.val=headC.next.val,headC.val
                    seen.add(headC)
                    seen.add(headC.next)
            headC=headC.next
        return head

if __name__=="__main__":
    head=ListNode(val=1,
                  next=ListNode(val=2,
                                next=ListNode(val=3,
                                              next=ListNode(val=4,
                                                            next=ListNode(val=5,
                                                                          next=None)))))   
    print(Solution().swapPairs(head=head))

