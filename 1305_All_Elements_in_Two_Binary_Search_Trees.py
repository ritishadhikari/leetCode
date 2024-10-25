from typing import List,Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        ans=[]
        leftSeen,rightSeen=set(),set()
        if root1: 
            leftStack=[root1]
            while root1.left:
                root1=root1.left
                leftStack.append(root1)
        else: leftStack=[]
        if root2: 
            rightStack=[root2]
            while root2.left:
                root2=root2.left
                rightStack.append(root2)
        else: rightStack=[]
        
        
        
        while leftStack or rightStack:
            if leftStack:
                if leftStack[-1].left and leftStack[-1].left not in leftSeen:
                    root=leftStack[-1]
                    while root.left:
                        leftStack.append(root.left)
                        root=root.left
                smallestLeft=leftStack.pop()
            else:
                smallestLeft=None
            if rightStack:
                if rightStack[-1].left and rightStack[-1].left not in rightSeen:
                    root=rightStack[-1]
                    while root.left:
                        rightStack.append(root.left)
                        root=root.left
                smallestRight=rightStack.pop()
            else:
                smallestRight=None
            if smallestLeft is not None and smallestRight is not None:
                if smallestLeft.val<smallestRight.val:
                    ans.append(smallestLeft.val)
                    leftSeen.add(smallestLeft)
                    rightStack.append(smallestRight)
                    if smallestLeft.right:
                        leftStack.append(smallestLeft.right)
                else:
                    ans.append(smallestRight.val)
                    rightSeen.add(smallestRight)
                    leftStack.append(smallestLeft)
                    if smallestRight.right:
                        rightStack.append(smallestRight.right)
            elif smallestLeft is None and smallestRight is not None :
                ans.append(smallestRight.val)
                rightSeen.add(smallestRight)
                if smallestRight.right:
                    rightStack.append(smallestRight.right)
            elif smallestRight is None and smallestLeft is not None :
                ans.append(smallestLeft.val)
                leftSeen.add(smallestLeft)
                if smallestLeft.right:
                    leftStack.append(smallestLeft.right)
        return ans






if __name__=="__main__":
    root1=TreeNode(val=2,
                   left=TreeNode(val=1,
                                 left=None,
                                 right=None),
                    right=TreeNode(val=4,
                                   left=None,
                                   right=None)
                    )
    root2=TreeNode(val=1,
                   left=TreeNode(val=0,
                                 left=None,
                                 right=None),
                    right=TreeNode(val=3,
                                   left=None,
                                   right=None)
                    )
    print(Solution().getAllElements(root1=root1,root2=root2))