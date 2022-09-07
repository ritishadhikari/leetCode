from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count=0
        seenleftNode=set()
        stack=[root]
        while stack:
            node=stack[-1]
            if node.left and node not in seenleftNode:
                stack.append(node.left)
                seenleftNode.add(node)
            else:
                node=stack.pop()
                count+=1
                if count==k:
                    return node.val
                if node.right:
                    stack.append(node.right)

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

    print(Solution().kthSmallest(root=root,k=3))
