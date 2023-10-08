from typing import List, Optional

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        count=0
        last=None
        lastC=None
        stack=[(root,count)]
        while stack and stack[0][0]:
            node,countL=stack.pop(0)
            if node.left:
                stack.append((node.left,countL+1))
            if node.right:
                stack.append((node.right,countL+1))
            if lastC is not None:
                if lastC==countL:
                    last.next=node
                else:
                    last.next=None
                
            lastC=countL
            last=node

        if last:
            last.next=None
        
        return root

if __name__=="__main__":
    root=Node(
        val=1,
              left=Node(val=2,
                        left=Node(val=4,
                                  left=None,
                                  right=None,
                                  next=None),
                        right=Node(val=5,
                                   left=None,
                                   right=None,
                                   next=None),
                        next=None
                        ),
              right=Node(val=3,
                         left=None,
                         right=Node(val=7,
                                    left=None,
                                    right=None,
                                    next=None),
                         next=None

                         )
              
              )
    print(Solution().connect(root=root))