from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        levelSum={}
        level=0
        stack=[(root,level)]
        while stack:
            node,level=stack.pop(0)
            if level not in levelSum:
                levelSum[level]=node.val
            else:
                levelSum[level]+=node.val
            if node.left is not None or node.right is not None:
                level+=1
                if node.left is not None:
                    stack.append((node.left,level))
                if node.right is not None:
                    stack.append((node.right,level))
        return levelSum[max(levelSum.keys())]
if __name__=="__main__":
    root=TreeNode(val=6,
                  left=TreeNode(val=7,
                                left=TreeNode(val=2,
                                              left=TreeNode(val=9,
                                                            left=None,
                                                            right=None),
                                              right=None),
                                right=TreeNode(val=7,
                                               left=TreeNode(val=1,
                                                             left=None,
                                                             right=None),
                                               right=TreeNode(val=4,
                                                              left=None,
                                                              right=None)
                                               )
                                ),
                  right=(TreeNode(val=8,
                                left=TreeNode(val=1,
                                                left=None,
                                                right=None),
                                right=TreeNode(val=3,
                                               left=None,
                                               right=TreeNode(val=5,
                                                              left=None,
                                                              right=None))
                                ))
                    )
    print(Solution().deepestLeavesSum(root=root))