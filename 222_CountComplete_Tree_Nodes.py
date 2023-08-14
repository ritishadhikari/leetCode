from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        stack=[root]
        count=0
        while stack and stack[0]:
            node=stack.pop()
            count+=1
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return count

if __name__=="__main__":
    root=TreeNode(
        val=3,
        left=TreeNode(val=5,
                      left=TreeNode(val=6,
                                    left=None,
                                    right=None),
                      right=TreeNode(val=2,
                                     left=TreeNode(val=7,
                                                   left=None,
                                                   right=None),
                                     right=TreeNode(val=4,
                                                    left=None,
                                                    right=None)           
                                                   )
                                    ),
        right=TreeNode(val=1,
                       left=TreeNode(val=0,
                                     left=TreeNode(val=9,
                                                   left=None,
                                                   right=None),
                                     right=None
                                     ),
                       right=TreeNode(val=8,
                                      left=None,
                                      right=TreeNode(val=10,
                                                     left=None,
                                                     right=None))
                                                   )                
    )              
    print(Solution().countNodes(root=root))