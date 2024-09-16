from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        tracker={}
        stack=[root]
        while stack:
            node=stack.pop()
            if node.left:
                stack.append(node.left)
                tracker[node.left]=[node.val]
                if node in tracker:
                    tracker[node.left].extend(tracker[node])
            if node.right:
                stack.append(node.right)
                tracker[node.right]=[node.val]
                if node in tracker:
                    tracker[node.right].extend(tracker[node])

        lst=[]
        for node,vals in tracker.items():
            lst.append(max([abs(node.val-i) for i in vals]))
        return max(lst)




if __name__=="__main__":
    # root=TreeNode(val=8,
    #               left=TreeNode(val=3,
    #                             left=TreeNode(val=1,
    #                                           left=None,
    #                                           right=None),
    #                             right=TreeNode(val=6,
    #                                            left=TreeNode(left=TreeNode(val=4,
    #                                                                        left=None,
    #                                                                        right=None),
    #                                                         right=TreeNode(val=7,
    #                                                                        left=None,
    #                                                                        right=None)))
    #                             ),
    #             right=TreeNode(val=10,
    #                            left=None,
    #                            right=TreeNode(val=14,
    #                                           left=TreeNode(val=13,
    #                                                         left=None,
    #                                                         right=None),
    #                                           right=None))
    #     )
    root=TreeNode(val=1,
                  left=None,
                  right=TreeNode(val=2,
                                 left=None,
                                 right=TreeNode(val=0,
                                                left=TreeNode(val=3,
                                                              left=None,
                                                              right=None),
                                                right=None)))
    print(Solution().maxAncestorDiff(root=root))