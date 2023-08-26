# VVI
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        h1=l1=ListNode(val=0)
        h2=l2=ListNode(val=0)

        while head:
            if head.val<x:
                l1.next=head
                l1=l1.next
            else:
                l2.next=head
                l2=l2.next
            head=head.next
        l2.next=None
        l1.next=h2.next
        return h1.next

if __name__=="__main__":
    head=ListNode(val=1, 
                  next=ListNode(val=4,
                                next=ListNode(val=3,
                                              next=ListNode(val=2,
                                                            next=ListNode(val=5,
                                                                     next=ListNode(val=2,
                                                                                   next=None))))))
    x=3
    
    print(Solution().partition(head=head,x=x))