from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.currentNode=root
        self.stack=[]

    def next(self) -> int:
        while self.currentNode:
            self.stack.append(self.currentNode)
            self.currentNode=self.currentNode.left
        
        next=self.stack.pop()
        self.currentNode=next.right
        
        return next.val


    def hasNext(self) -> bool:
        if self.currentNode or self.stack:
            return True
        else:
            return False

if __name__=="__main__":
    root=TreeNode(val=5,
                left=TreeNode(val=3,
                            left=TreeNode(val=2,
                                        left=TreeNode(val=1,
                                                    left=None,
                                                    right=None),
                                        right=None),
                            right=TreeNode(val=4,
                                        left=None,
                                        right=None)),
                right=TreeNode(val=6,
                            left=None,
                            right=None))
    obj=BSTIterator(root=root)
    print(obj.next())
    print(obj.hasNext())
    print(obj.next())
    print(obj.next())
    print(obj.next())
    print(obj.hasNext())
    print(obj.next())
    print(obj.next())
    print(obj.hasNext())