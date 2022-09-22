from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        stackP=[p]
        stackQ=[q]
        while stackP and stackQ and stackP[-1] and stackQ[-1]:
            P=stackP.pop()
            Q=stackQ.pop()
            if P:
                pVal=P.val
            else:
                pVal=None
            if Q:
                qVal=Q.val
            else:   
                qVal=None
            if not pVal==qVal:
                return False
            else:
                if P.right and Q.right:
                    stackP.append(P.right)
                    stackQ.append(Q.right)
                else:
                    if (P.right and not Q.right) or (not P.right and Q.right):
                        return False
                if P.left and Q.left:
                    stackP.append(P.left)
                    stackQ.append(Q.left)
                else:
                    if (P.left and not Q.left) or (not P.left and Q.left):
                        return False
        if (stackP and not stackQ) or (stackQ and not stackP) or (stackP[-1] and stackQ[-1]) :
            return False
        else:
            return True

if __name__=="__main__":
    p=TreeNode(val=1,
            left=TreeNode(val=2,
                        left=None,
                        right=None),
            right=TreeNode(val=1,
                        left=None,
                        right=None))
    q=TreeNode(val=1,
            left=TreeNode(val=1,
                        left=None,
                        right=None),
            right=TreeNode(val=2,
                        left=None,
                        right=None))
    print(Solution().isSameTree(p=p,q=q))
        