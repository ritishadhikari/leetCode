from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        rootc=root
        stack=[root]
        seen=set()
        seen.add(root)
        t2s={}
        while stack:
            pn=stack[-1]
            if (pn.left and pn.left not in seen) or (pn.right and pn.right not in seen):
                if pn.left:
                    t2s[pn.left]=pn
                    seen.add(pn.left)
                    stack.append(pn.left)
                if pn.right:
                    t2s[pn.right]=pn
                    seen.add(pn.right)
                    stack.append(pn.right)
            elif pn.left is None and pn.right is None:
                node=stack.pop()
                if node.val==target:
                    if node not in t2s:  # have reached the root node which equals the target
                        return None
                    else:
                        if t2s[node].right==node:
                            t2s[node].right=None
                        else:
                            t2s[node].left=None
            else:
                stack.pop()
        return rootc


if __name__=="__main__":
    # root=TreeNode(val=1,
    #               left=TreeNode(val=2,
    #                             left=TreeNode(val=2,
    #                                           left=None,
    #                                           right=None),
    #                             right=TreeNode(val=2,
    #                                            left=TreeNode(val=4,
    #                                                          left=None,
    #                                                          right=None),
    #                                             right=TreeNode(val=5,
    #                                                            left=None,
    #                                                            right=None))
    #                             ),
    #               right=TreeNode(val=2,
    #                              left=TreeNode(val=2,
    #                                            left=TreeNode(val=2,
    #                                                          left=None,
    #                                                          right=None),
    #                                             right=TreeNode(val=2,
    #                                                          left=None,
    #                                                          right=None)
    #                                                          ),
    #                              right=TreeNode(val=2,
    #                                             left=None,
    #                                             right=None)
    #                             )
    #               )
    # target=2
    root=TreeNode(val=1,
                  left=TreeNode(val=2,
                                left=TreeNode(val=2,
                                              left=None,
                                              right=None)),
                  right=TreeNode(val=3,
                                 left=TreeNode(val=2,
                                               left=None,
                                               right=None),
                                right=TreeNode(val=4,
                                               left=None,
                                               right=None))
                )
    target=2
    print(Solution().removeLeafNodes(root=root,target=target))