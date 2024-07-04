from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans=None
        while head:
            if head.val==0 and head.next is not None:
                if ans is None:
                    ans=ListNode(val=0,
                                 next=None)
                    ansCopy=ans
                else:
                    ansCopy.next=ListNode(val=head.val,
                                      next=None)
                    ansCopy=ansCopy.next
            else:
                ansCopy.val+=head.val
            head=head.next
        return ans

if __name__=="__main__":
    head=ListNode(val=0,
                  next=ListNode(val=1,
                                next=ListNode(val=0,
                                              next=ListNode(val=3,
                                                            next=ListNode(val=0,
                                                                          next=ListNode(val=2,
                                                                                        next=ListNode(val=2,
                                                                                                      next=ListNode(val=0,
                                                                                                                    next=None))))))))
    
    print(Solution().mergeNodes(head=head))