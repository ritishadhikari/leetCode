from typing import Optional, List
from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        stack=[root]
        lastNode=None
        node=root
        val=0
        container=defaultdict()
        while stack and stack[-1] or node:
            if node and node.left:
                if val:  
                    val=max(val-1,0)
                node=node.left
                stack.append(node)
            else:
                node=stack[-1]
                if node.right and node.right!=lastNode:
                    stack.append(node.right)
                    val=max(val-1,0)
                    node=node.right
                else:
                    node=stack.pop()
                    container[val]=node.val
                    val+=1
                    lastNode=node
                    node=None
        return list(container.values())[::-1] if container else []



if __name__=="__main__":
    root=TreeNode(val=5,
                left=TreeNode(val=3,
                            left=TreeNode(val=2,
                                        left=TreeNode(val=1,
                                                    left=None,
                                                    right=None),
                                        right=None),
                            right=TreeNode(val=4,
                                        left=None,
                                        right=None)),
                right=TreeNode(val=6,
                            left=None,
                            right=None))
    print(Solution().rightSideView(root=root))