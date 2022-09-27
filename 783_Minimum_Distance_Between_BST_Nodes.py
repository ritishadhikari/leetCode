# Definition for a binary tree node.
from typing import Optional
from math import inf
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        minVal=inf
        stack=deque([root])
        while stack:
            node=stack.popleft()
            if node.right:
                minVal=min(abs(node.val-node.right.val),minVal)
                stack.appendleft(node.right)
            if node.left:
                minVal=min(abs(node.val-node.left.val),minVal)
                stack.appendleft(node.left)
        return minVal

            

if __name__=="__main__":
    root=TreeNode(val=4,
                left=TreeNode(val=2,
                            left=TreeNode(val=1,
                                    left=None,
                                    right=None),
                            right=TreeNode(val=3,
                                    left=None,
                                    right=None)),
                right=TreeNode(val=6,
                            left=None,
                            right=None))

    print(Solution().minDiffInBST(root=root))