from typing import Optional
from collections import deque
class Node:
    def __init__(self, val:int=0,left:'Node'=None,
                right:'Node'=None,next:'Node'=None):
                self.val=val
                self.left=left
                self.right=right
                self.next=next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root
        stack=deque([root])  # Creating a Stack
        while stack:
            sizeofStack=len(stack)  # Size of stack
            i=0  # Maintaining a Counter
            while i<sizeofStack:
                node=stack.popleft()  # Creating a Node
                if node:
                    if i==sizeofStack-1:
                        node.next=None
                    else: 
                        node.next=stack[0]  # Storing Tree for Nodes Next Value
                    if node.left:
                        stack.append(node.left)
                    if node.right:
                        stack.append(node.right)
                i+=1
        return root

if __name__=="__main__":
    bt=Node(val=1,
            left=Node(val=2,
                     left=Node(val=4),right=Node(val=5)),
            right=Node(val=3,
                       left=Node(val=6), right=Node(7)))

    print(Solution().connect(root=bt))