from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        answer=[]
        stack=[(root,str(root.val))]
        while stack:
            item=stack.pop()
            node,string=item
            if node.left is not None or node.right is not None:
                if node.left:
                    stack.append((node.left,string+"->"+str(node.left.val)))
                if node.right:
                    stack.append((node.right,string+"->"+str(node.right.val)))
            else:
                answer.append(string)
        return answer

if __name__=="__main__":
    root=TreeNode(val=1,
                  left=TreeNode(val=2,
                                left=None,
                                right=TreeNode(val=5,
                                               left=None,
                                               right=None)),
                  right=TreeNode(val=3,
                                 left=None,
                                 right=None)   
                                               )
    print(Solution().binaryTreePaths(root=root))