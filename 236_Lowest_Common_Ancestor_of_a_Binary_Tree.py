class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, 
                             root: 'TreeNode', 
                             p: 'TreeNode', q: 'TreeNode') -> TreeNode:
        stack=[root]
        tracker={}
        tracker[root.val]=[root.val]
        pReceived=False
        qReceived=False
        
        while stack and stack[0]:
            node=stack.pop()

            if node.val==p:
                pReceived=True
                if qReceived:
                    pAncestors=tracker[node.val]
                    qAncestors=tracker[q]
                    for ancestor in pAncestors:
                        if ancestor in set(qAncestors):
                            return ancestor
        
            elif node.val==q:
                qReceived=True
                if pReceived:
                    qAncestors=tracker[node.val]
                    pAncestors=tracker[p]
                    for ancestor in qAncestors:
                        if ancestor in set(pAncestors):
                            return ancestor

            if node.left:
                tracker[node.left.val]=[node.left.val] + tracker[node.val]
                stack.append(node.left)
            if node.right:
                tracker[node.right.val]=[node.right.val]+ tracker[node.val]
                stack.append(node.right)
            
    

if __name__=="__main__":
    root=TreeNode(
        val=3,
        left=TreeNode(val=5,
                      left=TreeNode(val=6,
                                    left=None,
                                    right=None),
                      right=TreeNode(val=2,
                                     left=TreeNode(val=7,
                                                   left=None,
                                                   right=None),
                                     right=TreeNode(val=4,
                                                    left=None,
                                                    right=None)           
                                                   )
                                    ),
        right=TreeNode(val=1,
                       left=TreeNode(val=0,
                                     left=TreeNode(val=9,
                                                   left=None,
                                                   right=None),
                                     right=None
                                     ),
                       right=TreeNode(val=8,
                                      left=None,
                                      right=TreeNode(val=10,
                                                     left=None,
                                                     right=None))
                                                   )                
    )              
    print(Solution().lowestCommonAncestor(root=root, p=2, q=8))