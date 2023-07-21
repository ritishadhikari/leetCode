from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        stack=[root]
        averageList=[]
        while stack:
            lengthOfStack=len(stack)
            value=0
            count=0
            while lengthOfStack:
                node=stack.pop(0)
                if node:
                    value+=node.val
                    count+=1
                    if node.left: 
                        stack.append(node.left)
                    if node.right:
                        stack.append(node.right)
                    lengthOfStack-=1
                    if lengthOfStack==0:
                        averageList.append(value/count)
        return averageList

if __name__=="__main__":
    root=TreeNode(val=3,
                  left=TreeNode(val=9,
                                left=None,
                                right=None),
                  right=TreeNode(val=20,
                                left=TreeNode(val=15,
                                            left=None,
                                            right=None),
                                right=TreeNode(val=7, 
                                               left=None,
                                               right=None)
                                               )             
                                )
    print(Solution().averageOfLevels(root=root))