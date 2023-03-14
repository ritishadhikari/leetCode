from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #step 1: find middle
        if not head: return []
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        #step 2: reverse second half
        prev, curr = None, slow.next
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt    
        slow.next = None
        
        #step 3: merge lists
        head1, head2 = head, prev
        while head2:
            nextt = head1.next
            head1.next = head2
            head1 = head2
            head2 = nextt

if __name__=="__main__":
    head=ListNode(val=1,  #s1,f1
                  next=ListNode(val=2,  #s2
                                next=ListNode(val=3,  #f2  #s3
                                              next=ListNode(val=4,
                                                            next=ListNode(val=5,  
                                                                          next=None #f3
                                                                    )))))
    
    print(Solution().reorderList(head=head))
    # [1,2,3,4,5]                                                                      
    # [1,2,3] [4,5] = [1,2,3] [5,4]
    # [1,5,2,4,3]
    # [1,_,2,_,3]
    # [1,5,]
    