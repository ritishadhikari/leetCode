from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack=[root]
        count=0
        rootc=root
        while root and (root.right or stack):
            if root.right is not None:
                root=root.right
                stack.append(root)
            elif root.right is None:
                value=stack.pop()
                count+=value.val
                value.val=count
                if value.left:
                    stack.append(value.left)
                    root=value.left
                
        return rootc

if __name__=="__main__":
    root=TreeNode(val=4,
                left=TreeNode(val=1,
                            left=TreeNode(val=0,
                                            left=None,
                                            right=None),
                            right=TreeNode(val=2,
                                        left=None,
                                        right=TreeNode(val=3,
                                                    left=None,
                                                    right=None),
                                            )
                                            ),
                right=TreeNode(val=6,
                            left=TreeNode(val=5,
                                            left=None,
                                            right=None),
                            right=TreeNode(val=7,
                                        left=None,
                                        right=TreeNode(val=8,
                                                    left=None,
                                                    right=None))    
                            )
                )
    print(Solution().convertBST(root=root))