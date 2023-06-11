from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root and root.val is not None:
            answer=[[root.val]]
            stack=[root]
            left,right=False,True
            while stack:
                stackLen=len(stack)
                resFromThisLevel=[]
                while stackLen>0:
                    node=stack.pop(0)
                    if not left and right:
                        if node.right:
                            resFromThisLevel.append(node.right.val)
                            stack.append(node.right)
                        if node.left:
                            resFromThisLevel.append(node.left.val)
                            stack.append(node.left)
                    else:
                        if node.left:
                            resFromThisLevel.append(node.left.val)
                            stack.append(node.left)
                        if node.right:
                            resFromThisLevel.append(node.right.val)
                            stack.append(node.right)   
                            
                    stackLen-=1
                    if stackLen==0:
                        if resFromThisLevel:
                            answer.append(resFromThisLevel)
                        stack.reverse()
                        left,right=right,left 
                    
            return answer


        else:
            return []

if __name__=="__main__":
    root=TreeNode(val=3,
                  left=TreeNode(val=9,
                                left=TreeNode(val=12,
                                              left=None,
                                              right=TreeNode(val=3,
                                                             left=None,
                                                             right=None)),
                                right=TreeNode(val=7, 
                                               left=None,
                                               right=TreeNode(val=12,
                                                              left=None,
                                                              right=None))),
                    right=TreeNode(val=20,
                                   left=TreeNode(val=15,
                                                 left=TreeNode(val=8,
                                                               left=None,
                                                               right=None),
                                                 right=TreeNode(val=7,
                                                                left=None,
                                                                right=None)),
                                    right=TreeNode(val=7, 
                                                   left=TreeNode(val=6,
                                                                 left=TreeNode(val=11,
                                                                               left=None,
                                                                               right=None)),
                                                    right=None
                                                    )
                                    )                                          
                                                              )
    print(Solution().zigzagLevelOrder(root=root))