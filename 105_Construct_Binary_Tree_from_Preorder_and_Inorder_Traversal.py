# VVI
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], 
                  inorder: List[int]) -> Optional[TreeNode]:
        tracker={x:i for i,x in enumerate(inorder)}
        stack=[]
        root=None
        for x in preorder:
            if root is None:
                root=TreeNode(val=x)
                node=root
            elif tracker[x]<tracker[node.val]:
                stack.append(node)
                node.left=TreeNode(val=x)
                node=node.left
            else: 
                while stack and tracker[x]>tracker[stack[-1].val]:
                    node=stack.pop()
                node.right=TreeNode(val=x)
                node=node.right
        return root


if __name__=="__main__":
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    print(Solution().buildTree(preorder=preorder, inorder=inorder))