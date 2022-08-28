from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        addOdd,addEven=None,None
        condition="odd"
        while head:
            if condition=="odd":
                if not addOdd:
                    actualOdd=ListNode(val=head.val,next=ListNode())
                    addOdd=actualOdd
                else:
                    addOdd=addOdd.next
                    addOdd.val=head.val
                    addOdd.next=ListNode()         
                condition="even"
            else:
                if not addEven:
                    actualEven=ListNode(val=head.val,next=ListNode())
                    addEven=actualEven
                else:
                    addEven=addEven.next
                    addEven.val=head.val
                    addEven.next=ListNode()
                condition="odd"
            head=head.next        
        if addOdd:
            if addEven:
                addEven.next=None
                addOdd.next=actualEven
            else:
                addOdd.next=None
            return actualOdd
        else:
            return None
                





if __name__=="__main__":
    head=ListNode(val=1,next=ListNode(val=2,next=ListNode(val=3,next=ListNode(val=4,next=None))))
    head=ListNode(val=1,next=None)
    print(Solution().oddEvenList(head=head))

"""
328. Odd Even Linked List
[1,2,3,4]

addOdd=None
addEven=None

condition='odd'
actualOdd=ListNode(val=1,next=ListNode(val=None,next=None))
addOdd=actualOdd	
# actualOdd=ListNode(val=1,next=ListNode(val=None,next=None))

condition="even"
actualEven=ListNode(val=2,next=ListNode(val=None, next=None))
addEven=actualEven
# actualEven=ListNode(val=2,next=ListNode(val=None, next=None))

condition="odd"
addOdd=addOdd.next
addOdd=ListNode(val=3,next=ListNode(val=None, next=None)) 
# actualOdd=ListNode(val=1,next=ListNode(val=3,next=ListNode(val=None, next=None)))
	
condition="even"
addEven=addEven.next
addEven=ListNode(val=4, next=ListNode(val=None, next=None))
# actualEven=ListNode(val=2,next=ListNode(val=4, next=ListNode(val=None, next=None)))

# actualOdd=ListNode(val=1,next=ListNode(val=3,next=ListNode(val=None, next=None)))
# actualEven=ListNode(val=2,next=ListNode(val=4, next=ListNode(val=None, next=None)))

addEven.next=None
# actualEven=ListNode(val=2,next=ListNode(val=4, next=None)))
addOdd.next=actualEven

# actualOdd=ListNode(val=1,next=ListNode(val=3,next=ListNode(val=2,next=ListNode(val=4, next=None)))))

"""