from typing import List, Optional
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

from copy import deepcopy
class Solution:
    def middleNode(self,head:Optional[ListNode]) -> Optional[ListNode]:
        
        tempHead=head  #Ritish's Solution
        count=0
        while tempHead:
            count+=1
            tempHead=tempHead.next  
        
        i=0
        while i<count//2:
            i+=1
            head=head.next 

        return head

        # Alternate Solution

        # tempHead=head
        # while tempHead and tempHead.next:
        #   head=head.next
        #   temphead=tempHead.next.next
        
        # return head


a=ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6,None))))))

if __name__=="__main__":
    print(Solution().middleNode(head=a))
