from typing import Optional
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
                   
        def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
            if not root1:
                return root2
            if not root2:
                return root1
            
            stack1=collections.deque([root1])
            stack2=collections.deque([root2])

            while stack1 and stack2:
                node1=stack1.popleft()
                node2=stack2.popleft()
                if node1 and node2:
                    node1.val=node1.val+node2.val

                    if not node1.left and node2.left:
                        node1.left=TreeNode(val=0)
                    if not node1.right and node2.right:
                        node1.right=TreeNode(val=0)
                
                    stack1.append(node1.left)
                    stack1.append(node1.right)

                    stack2.append(node2.left)
                    stack2.append(node2.right)

            return root1
                

            


  

if __name__=="__main__":
    print(Solution().mergeTrees(root1=TreeNode(val=1,
                                            left=TreeNode(val=3,left=TreeNode(val=5)),
                                            right=TreeNode(val=2,left=None, right=None)),
                                root2=TreeNode(val=2,
                                            left=TreeNode(val=1,left=None,right=TreeNode(4)),
                                            right=TreeNode(val=3,left=None,right=TreeNode(val=7)))))
