class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next
"""
1 2 3 4 5 None -> 5 4 3 2 1 None

None               1 2 3 4 5 None

1 None             2 3 4 5 None

2 1 None           3 4 5 None

3 2 1 None         4 5 None

4 3 2 1 None       5 None

5 4 3 2 1 None     None

"""

class Solution:
    def reverseList(self, head):
        start=None
        while head:
            start=ListNode(val=head.val, next=start)
            head=head.next
        return start

if __name__=="__main__":
    ll=ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,None)))))
    print(Solution().reverseList(head=ll))