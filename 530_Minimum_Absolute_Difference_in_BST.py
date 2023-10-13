from typing import List, Optional
from math import inf
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack=set()
        ans=inf
        if root:
            if root.left:
                stack.add((root,root.left,"r"))
            if root.right:
                stack.add((root,root.right,"l"))
            while stack:
                node1,node2,direction=stack.pop()
                ans=min(ans,abs(node1.val-node2.val))
                if direction=="r":
                    if node2.right:
                        stack.add((node1,node2.right,"r"))
                        stack.add((node2,node2.right,"l"))
                    if node2.left:
                        stack.add((node2,node2.left,"r"))
                elif direction=="l":
                    if node2.left:
                        stack.add((node1,node2.left,"l"))
                        stack.add((node2,node2.left,"r"))
                    if node2.right:
                        stack.add((node2,node2.right,"l"))
                        
            return ans



if __name__=="__main__":
    root=TreeNode(val=23,
                  left=TreeNode(val=11,
                                left=TreeNode(val=5,
                                              left=TreeNode(val=1,
                                                            left=None,
                                                            right=None),
                                              right=TreeNode(val=8,
                                                             left=None,
                                                             right=None)
                                              ),
                                right=TreeNode(val=17,
                                               left=TreeNode(val=14,
                                                             left=None,
                                                             right=None),
                                               right=TreeNode(val=20,
                                                              left=None,
                                                              right=None)
                                               )
                                ),
                  right=TreeNode(val=40,
                                 left=TreeNode(val=30,
                                               left=None,
                                               right=None),
                                 right=TreeNode(val=42,
                                                left=None,
                                                right=None)
                                 )
                  )
    print(Solution().getMinimumDifference(root=root))