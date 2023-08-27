from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        stack=[root]
        sumVal=0 
        while stack and stack[0]:
            node=stack.pop(0)
            if node.left is None and node.right is None:
                sumVal+=node.val
            else:
                if node.left:
                    node.left.val+=node.val*10
                    stack.append(node.left)
                if node.right:
                    node.right.val+=node.val*10
                    stack.append(node.right)
        return sumVal
if __name__=="__main__":
    root=TreeNode(val=4, 
             left=TreeNode(val=9,
                           left=TreeNode(val=5,
                                         left=TreeNode(val=2,
                                                       left=None,
                                                       right=None),
                                         right=TreeNode(val=8,
                                                        left=None,
                                                        right=None)
                                            ),
                           right=TreeNode(val=1,
                                          left=TreeNode(val=2,
                                                        left=None,
                                                        right=None),
                                          right=None
                                        )
                    ),
             right=TreeNode(val=0,
                            left=TreeNode(val=3,
                                          left= None,
                                          right=None
                                          ),
                            right=TreeNode(val=2,
                                           left=None,
                                           right=TreeNode(val=6,
                                                          left=None,
                                                          right=None))
                            )
                    )
    
    print(Solution().sumNumbers(root=root))