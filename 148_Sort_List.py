from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst=[]
        while head is not None:
            lst.append(head.val)
            head=head.next
        lst.sort()

        if len(lst)==0: 
            return None
        
        if len(lst)<=2:
            if len(lst)==1:
                return ListNode(val=lst[0])
            elif len(lst)==2:
                return ListNode(val=lst[0], next=ListNode(val=lst[1], next=None))
        else:
            M=ListNode(val=lst[0], next=ListNode(val=lst[1],next=None))
            K=M
            K=K.next
            for i,v in enumerate(lst[2:]):
                K.next=ListNode(val=v,next=None)
                K=K.next
            return M

if __name__=="__main__":
    head=ListNode(val=-1,
                  next=ListNode(val=5,
                                next=ListNode(val=3,
                                              next=ListNode(val=4,
                                                            next=ListNode(val=0,
                                                                          next=None)))))
    print(Solution().sortList(head=head))