# VVI
from re import T
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution():
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        stack=[]
        node=root
        depth={}
        last=None
        while stack or node:
            if node:
                stack.append(node)
                node=node.right
            else:
                node=stack[-1]
                if node.left is None or node.left==last:
                    node=stack.pop()
                    left=depth.get(node.left,0)
                    right=depth.get(node.right,0)
                    if abs(left-right)>1:
                        return False
                    else:
                        depth[node]=max(left,right)+1
                    last=node
                    node=None
                else:
                    node=node.left
        return True

if __name__=="__main__":
    root=TreeNode(val=3, 
                  left=TreeNode(val=9,
                                left=TreeNode(val=38, 
                                              left=TreeNode(val=42, 
                                                            left=None, 
                                                            right=None), 
                                              right=TreeNode(val=29,
                                                             left=None,
                                                             right=None)),
                                right=None), 
				  right=TreeNode(val=25,
                                 left=TreeNode(val=17,
                                               left=TreeNode(val=41,
                                                             left=TreeNode(val=30,
                                                                           left=None,
                                                                           right=None),
                                                             right=TreeNode(val=40,
                                                                            left=None,
                                                                            right=None)),
                                               right=TreeNode(val=52,
                                                              left=None,
                                                              right=None
                                                                )),
                                 right=TreeNode(val=32,
                                                left=TreeNode(val=15,
                                                              left=None,
                                                              right=None),
                                                right=None)


                  )
    )
    print(Solution().isBalanced(root=root))

    '''
            WORKING:
            stack=[]
        node=TreeNode(val=3, left=TreeNode(9,TreeNode(38, TreeNode(42, None, None), TreeNode(29,None,None)),None), 
                        right=TreeNode(25,TreeNode(17, TreeNode(4, TreeNode(30,None,None)),TreeNode(52, None,None)),TreeNode(32,None,None)))
        last=None
        depths={}

        stack=[TreeNode(val=3, left=TreeNode(9,TreeNode(38, TreeNode(42, None, None), TreeNode(29,None,None)),None), 
                        right=TreeNode(25,TreeNode(17, TreeNode(4, TreeNode(30,None,None)),TreeNode(52, None,None)),TreeNode(32,None,None)))]
        node=TreeNode(9,TreeNode(38, TreeNode(42, None, None), TreeNode(29,None,None)),None)

        stack=[
                TreeNode(val=3, left=TreeNode(9,TreeNode(38, TreeNode(42, None, None), TreeNode(29,None,None)),None), 
                        right=TreeNode(25,TreeNode(17, TreeNode(4, TreeNode(30,None,None)),TreeNode(52, None,None)),TreeNode(32,None,None))),
                TreeNode(9,TreeNode(38, TreeNode(42, None, None), TreeNode(29,None,None)),None)
                ]
        node=TreeNode(38, TreeNode(42, None, None), TreeNode(29,None,None))

        stack=[
                TreeNode(val=3, left=TreeNode(9,TreeNode(38, TreeNode(42, None, None), TreeNode(29,None,None)),None), 
                        right=TreeNode(25,TreeNode(17, TreeNode(4, TreeNode(30,None,None)),TreeNode(52, None,None)),TreeNode(32,None,None))),
                TreeNode(9,TreeNode(38, TreeNode(42, None, None), TreeNode(29,None,None)),None),
                TreeNode(38, TreeNode(42, None, None), TreeNode(29,None,None))
                
                ]
        node=TreeNode(42, None, None)

        stack=[
                TreeNode(val=3, left=TreeNode(9,TreeNode(38, TreeNode(42, None, None), TreeNode(29,None,None)),None), 
                        right=TreeNode(25,TreeNode(17, TreeNode(4, TreeNode(30,None,None)),TreeNode(52, None,None)),TreeNode(32,None,None))),
                TreeNode(9,TreeNode(38, TreeNode(42, None, None), TreeNode(29,None,None)),None),
                TreeNode(38, TreeNode(42, None, None), TreeNode(29,None,None))
                TreeNode(42, None, None)
                ]
        node=None

        -----
        node=TreeNode(42, None, None)
        node=TreeNode(42, None, None)
        stack=[
                TreeNode(val=3, left=TreeNode(9,TreeNode(38, TreeNode(42, None, None), TreeNode(29,None,None)),None), 
                        right=TreeNode(25,TreeNode(17, TreeNode(4, TreeNode(30,None,None)),TreeNode(52, None,None)),TreeNode(32,None,None))),
                TreeNode(9,TreeNode(38, TreeNode(42, None, None), TreeNode(29,None,None)),None),
                TreeNode(38, TreeNode(42, None, None), TreeNode(29,None,None))
                ]
        left=0
        right=0
        depths={TreeNode(42, None, None):1}
        last=TreeNode(42, None, None)
        node=None
        -----
        node=TreeNode(38, TreeNode(42, None, None), TreeNode(29,None,None))
        node=TreeNode(29,None,None)
        stack=[
                TreeNode(val=3, left=TreeNode(9,TreeNode(38, TreeNode(42, None, None), TreeNode(29,None,None)),None), 
                        right=TreeNode(25,TreeNode(17, TreeNode(4, TreeNode(30,None,None)),TreeNode(52, None,None)),TreeNode(32,None,None))),
                TreeNode(9,TreeNode(38, TreeNode(42, None, None), TreeNode(29,None,None)),None),
                TreeNode(38, TreeNode(42, None, None), TreeNode(29,None,None)),
                TreeNode(29,None,None)
                ]
        node=None
        -----
        node=TreeNode(29,None,None)
        node=TreeNode(29,None,None)
        stack=[
                TreeNode(val=3, left=TreeNode(9,TreeNode(38, TreeNode(42, None, None), TreeNode(29,None,None)),None), 
                        right=TreeNode(25,TreeNode(17, TreeNode(4, TreeNode(30,None,None)),TreeNode(52, None,None)),TreeNode(32,None,None))),
                TreeNode(9,TreeNode(38, TreeNode(42, None, None), TreeNode(29,None,None)),None),
                TreeNode(38, TreeNode(42, None, None), TreeNode(29,None,None))
                ]
        left=0
        right=0
        depths={TreeNode(42, None, None):1,
                TreeNode(29,None,None):1}
        last=TreeNode(29,None,None)
        node=None
        -----
        node=TreeNode(38, TreeNode(42, None, None), TreeNode(29,None,None))
        node=TreeNode(38, TreeNode(42, None, None), TreeNode(29,None,None))
        stack=[
                TreeNode(val=3, left=TreeNode(9,TreeNode(38, TreeNode(42, None, None), TreeNode(29,None,None)),None), 
                        right=TreeNode(25,TreeNode(17, TreeNode(4, TreeNode(30,None,None)),TreeNode(52, None,None)),TreeNode(32,None,None))),
                TreeNode(9,TreeNode(38, TreeNode(42, None, None), TreeNode(29,None,None)),None),
                ]
        left=1
        right=1
        depths={
                TreeNode(42, None, None):1,
                TreeNode(29,None,None):1,
                TreeNode(38, TreeNode(42, None, None), TreeNode(29,None,None)):2
                }
        last=TreeNode(38, TreeNode(42, None, None), TreeNode(29,None,None))
        node=None
        -----
        node=TreeNode(9,TreeNode(38, TreeNode(42, None, None), TreeNode(29,None,None)),None)
        node=TreeNode(9,TreeNode(38, TreeNode(42, None, None), TreeNode(29,None,None)),None)
        stack=[
                TreeNode(val=3, left=TreeNode(9,TreeNode(38, TreeNode(42, None, None), TreeNode(29,None,None)),None), 
                        right=TreeNode(25,TreeNode(17, TreeNode(4, TreeNode(30,None,None)),TreeNode(52, None,None)),TreeNode(32,None,None)))
                ]
        left=2
        right=0
        return False as abs(left-right)>1
   
    '''