# VVI
from typing import Optional
from math import inf
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev=TreeNode(val=-inf)
        replace=[]
        stack=[]
        current=root
        while current or stack:
            while current:
                stack.append(current)
                current=current.left
            
            temp=stack.pop()
            if temp.val<prev.val:
                replace.append((prev,temp))
            prev=temp
            current=temp.right
        replace[0][0].val,replace[-1][1].val\
            =replace[-1][1].val,replace[0][0].val


if __name__=="__main__":
    root=TreeNode(val=14,
                  left=TreeNode(val=7,
                                left=TreeNode(val=3,
                                              left=None,
                                              right=None),
                                right=TreeNode(val=8,
                                               left=None,
                                               right=None)),
                  right=TreeNode(val=22,
                                 left=TreeNode(val=17,
                                               left=TreeNode(val=9,
                                                             left=None,
                                                             right=None),
                                               right=TreeNode(val=20,
                                                              left=None,
                                                              right=None)
                                               ),
                                 right=TreeNode(val=25,
                                                left=None,
                                                right=None)
                                 )              
                )
    print(Solution().recoverTree(root=root))