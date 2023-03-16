from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # reverse list

        def reverseList(ll):
            prev=None
            curr=ll
            while curr:
                nextt=curr.next
                curr.next=prev
                prev=curr
                curr=nextt
            return prev

        l1=reverseList(ll=l1)
        l2=reverseList(ll=l2)

        def countElements(ll):
            c=0
            while ll:
                c+=1
                ll=ll.next
            return c
        countArr=sorted([(countElements(ll=l1),l1),(countElements(ll=l2),l2)], key=lambda k: k[0])

        biggerLL=countArr[-1][1]
        smallerLL=countArr[0][1]
        biggerCount=countArr[-1][0]

        carry=0
        addList=None
        while biggerCount>0:
            if smallerLL:
                val1=smallerLL.val
                smallerLL=smallerLL.next
            else:
                val1=0
            
            val2=biggerLL.val
            biggerLL=biggerLL.next

            total=(carry+val1+val2)%10
            carry=(carry+val1+val2)//10
           
            if addList is None:
                addList=ListNode(val=total, next=None)
                addListCopy=addList
            else:
                addListCopy.next=ListNode(val=total,next=None)
                addListCopy=addListCopy.next
            biggerCount-=1

        if carry:
            addListCopy.next=ListNode(val=carry,next=None)
        
        return reverseList(ll=addList)



if __name__=="__main__":
    l1=ListNode(val=2,
                next=ListNode(val=4,
                              next=ListNode(val=9,
                                            next=None)))

    l2=ListNode(val=2,
                next=ListNode(val=6,
                              next=ListNode(val=4,
                                            next=ListNode(val=9,
                                                          next=None))))
    
    l1=ListNode(val=9,
                next=ListNode(val=9,
                              next=None))
    l2=ListNode(val=1,
                next=None)
    print(Solution().addTwoNumbers(l1=l1,l2=l2))