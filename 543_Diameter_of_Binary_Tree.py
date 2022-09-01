from typing import Optional
from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        mv=0
        node=root
        stack=[]
        measureDict=defaultdict(lambda : -1)
        left=None
        while stack or node:
            if node:
                stack.append(node)
                node=node.left
            else:
                node=stack[-1]
                if node.right==None or node.right==left:
                    stack.pop()
                    lc=measureDict[node.left]
                    rc=measureDict[node.right]
                    measureDict[node]=max(lc+1,rc+1)
                    mv=max(mv,lc+rc+2)
                    left=node
                    node=None
                else:
                    node=node.right
        return mv

if __name__=="__main__":
    root=TreeNode(val=6,
                  left=TreeNode(val=3,
                                left=TreeNode(val=9,
                                              left=TreeNode(val=14,
                                                            left=None,
                                                            right=None),
                                              right=TreeNode(val=19,
                                                            left=None,
                                                            right=TreeNode(val=20,
                                                                          left=None,
                                                                          right=None))),
                                right=TreeNode(val=12,
                                               left=TreeNode(val=25,
                                                            left=None,
                                                            right=None),
                                               right=TreeNode(val=51,
                                                             left=TreeNode(val=50,
                                                                           left=None,
                                                                           right=None),
                                                             right=None))),
                  right=TreeNode(val=5,
                                 left=None,
                                 right=None))
    print(Solution().diameterOfBinaryTree(root=root))