from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        traceDict={}
        if not root: return 0
        else:
            stack=deque([root])
            traceDict[root]=1
            while stack:
                node=stack.popleft()
                if node.left is None and node.right is None:
                    return traceDict[node]
                else:
                    if node.left:
                        stack.append(node.left)
                        traceDict[node.left]=traceDict[node]+1
                    if node.right:
                        stack.append(node.right)
                        traceDict[node.right]=traceDict[node]+1


if __name__=="__main__":
    root=TreeNode(val=2, 
                left=None,
                right=TreeNode(val=3,
                            left=None,
                            right=TreeNode(val=4,
                                        left=None,
                                        right=TreeNode(val=5,
                                                    left=None,
                                                    right=TreeNode(val=6,
                                                                left=None,
                                                                right=None)
                                                    )
                                        )
                            )
                )

    root=TreeNode(val=1,
                left=TreeNode(val=2,
                            left=TreeNode(val=4,
                                        left=None,
                                        right=None),
                            right=TreeNode(val=3,
                                        left=None,
                                        right=None)
                            ),
                right=TreeNode(val=3,
                            left=None,
                            right=None)
                )
    print(Solution().minDepth(root=root))