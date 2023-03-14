# VVI
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # Check the number of elements
        fast,slow=head,head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
            
        # Reverse the second linked list
        previous=None
        current=slow.next
        while current:
            nexxt=current.next
            current.next=previous
            previous=current
            current=nexxt
        slow.next=None

        # merge both the linked list
        head1=head
        head2=previous
        while head2:
            nexxt=head1.next
            head1.next=head2
            head1=head2
            head2=nexxt

if __name__=="__main__":
    head=ListNode(val=1,
                  next=ListNode(val=2,
                                next=ListNode(val=3,
                                              next=ListNode(val=4,
                                                            next=ListNode(val=5,
                                                                          next=None)))))
    
    [1,5,2,4,3]
    [1,_,2,_,3]
    [1,5,]