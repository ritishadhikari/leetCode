from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack=[root]
        rootLevel=True
        rootCopy=root
        while stack and stack[0]:
            node=stack.pop(0)
            if node.right:
                stack.insert(0,node.right)
            if node.left:
                stack.insert(0,node.left)
            if not rootLevel:
                rootCopy.right=node
                rootCopy.left=None
                rootCopy=rootCopy.right
            elif rootLevel:
                rootLevel=False
            
            


if __name__=="__main__":
    root=TreeNode(val=1,
                  left=TreeNode(val=2,
                                left=TreeNode(val=4,
                                              left=None,
                                              right=None),
                                right=TreeNode(val=5,
                                               left=TreeNode(val=8,
                                                             left=None,
                                                             right=None),
                                               right=None
                                               )
                                ),
                  right=TreeNode(val=3,
                                 left=TreeNode(val=6,
                                               left=None,
                                               right=None),
                                 right=TreeNode(val=7,
                                                left=TreeNode(val=11,
                                                              left=None,
                                                              right=None),
                                                right=TreeNode(val=9,
                                                               left=None,
                                                               right=None)
                                                )
                                 )
                  )
    root=TreeNode(val=1,
                  left=TreeNode(val=2,
                                left=TreeNode(val=3,
                                              left=None,
                                              right=None),
                                right=TreeNode(val=4,
                                               left=None,
                                               right=None)),
                  right=TreeNode(val=5,
                                 left=None,
                                 right=TreeNode(val=6,
                                                left=None,
                                                right=None)))
    print(Solution().flatten(root=root))
