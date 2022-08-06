from typing import Optional

class ListNode:
    def __init__(self, x=0,next=None):
        self.val = x
        self.next = None
class Solution:
    def detectCycle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow2 = head
                while slow != slow2:
                    slow = slow.next
                    slow2 = slow2.next
                return slow


ll=ListNode(3,ListNode(2,ListNode(0,ListNode(-4,None))))
print(Solution().detectCycle(head=ll))