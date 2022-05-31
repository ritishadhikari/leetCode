from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # First Find Count of Nodes:
        count=0
        headTemp=head
        while headTemp:
            count+=1
            headTemp=headTemp.next
       

        elementToRemove=count-n+1
        
        if elementToRemove==1:
            return head.next
        else:
            tempHead=head
            i=1
            while i<elementToRemove:
                if i==elementToRemove-1:
                    tempHead.next=tempHead.next.next
                else:
                    tempHead=tempHead.next
                i+=1
            return head

if __name__=="__main__":
    h=ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,None)))))
    h=ListNode(1,next=None)
    print(Solution().removeNthFromEnd(head=h, n=1))