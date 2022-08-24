from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        pcheck=''
        while head:
            pcheck+=str(head.val)
            head=head.next
        return True if pcheck[::-1]==pcheck else False

head=ListNode(1,ListNode(2,ListNode(3,ListNode(1,None))))

print(Solution().isPalindrome(head=head))

