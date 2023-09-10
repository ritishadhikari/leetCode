from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        stack=[]
        root=None

        tracker={v:i for i,v in enumerate(inorder)}

        for x in postorder[::-1]:
            if root is None:
                root=TreeNode(val=x)
                node=root
                stack.append(node)
            elif tracker[x]>tracker[node.val]:
                    node.right=TreeNode(val=x)
                    stack.append(node)
                    node=node.right   
            else:
                while stack and tracker[x]<tracker[stack[-1].val]:
                    node=stack.pop()
                node.left=TreeNode(val=x)
                node=node.left
        
        return root




if __name__=="__main__":
    inorder = [9,3,15,20,7]
    postorder=[9,15,7,20,3]

    print(Solution().buildTree(inorder=inorder, postorder=postorder))