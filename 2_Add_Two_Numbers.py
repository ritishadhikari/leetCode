from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Count length of two linkedlist
        def getLength(ll) -> int:
            c=0
            while ll:
                c+=1
                ll=ll.next
            return c
        
        countList=sorted([(getLength(ll=l1),l1),(getLength(ll=l2),l2)],
                         key=lambda k: k[0],
                         reverse=True)
         
        # add the two linkedlist
        addList=None
        biggerList=countList[0][1]
        smallerList=countList[1][1]
        biggerCount=countList[0][0]
        carry=0
        while biggerCount>0:
            if smallerList:
                val1=smallerList.val
                smallerList=smallerList.next
            else:
                val1=0
            if biggerList:
                val2=biggerList.val
                biggerList=biggerList.next
            
            if carry+val1+val2>9:
                take=(carry+val1+val2)%10
                carry=(carry+val1+val2)//10
            else:
                take=val1+val2+carry
                carry=0

            if addList:
                addListCopy.next=ListNode(val=take,next=None)
                addListCopy=addListCopy.next
            else:
                addList=ListNode(val=take,next=None) 
                addListCopy=addList
            biggerCount-=1
        
        if carry:
            addListCopy.next=ListNode(val=carry,next=None)
        
        return addList

if __name__=="__main__":
    l1=ListNode(val=2,
                next=ListNode(val=4,
                              next=ListNode(val=3,
                                            next=None)))

    l2=ListNode(val=5,
                next=ListNode(val=6,
                              next=ListNode(val=4,
                                            next=None)))
    
    l1=ListNode(val=2,
                next=ListNode(val=4,
                              next=ListNode(val=9,
                                            next=None)))

    l2=ListNode(val=5,
                next=ListNode(val=6,
                              next=ListNode(val=4,
                                            next=ListNode(val=9,
                                                          next=None))))
    
    print(Solution().addTwoNumbers(l1=l1,l2=l2))