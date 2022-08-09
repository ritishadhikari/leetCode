## VVI
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        pre=None
        if root:
            stack=[root]
            root=root.left
        while stack or root:
            while root:
                stack.append(root)
                root=root.left
            node=stack.pop()
            if pre and pre.val>=node.val:
                return False
            pre=node
            root=node.right
        return True
        



        

if __name__=="__main__":

    tree=   TreeNode(val=10, 
                     left=TreeNode( val=6, 
                                    left=TreeNode(val=4,
                                                left=None,
                                                right=None),
                                    right=TreeNode(val=16,
                                                left=None,
                                                right=None)), 
                     right=TreeNode(val=15, 
                                    left=TreeNode(val=5,
                                                 left=None,
                                                 right=None),
                                    right=TreeNode(val=18,
                                                 left=None,
                                                 right=None)))


    tree=   TreeNode(val=2, 
                     left=None, 
                     right=TreeNode(val=5, 
                                    left=TreeNode(
                                            val=8,
                                            left=None,
                                            right=None),
                                    right=None))
   
    print(Solution().isValidBST(root=tree))
   
   
   
   
   
   
   
    