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
        # self.currentNode can be False when current node is at a right 
        # node and that right node is null but the stack may exist with
        # parent nodes
        # self.stack can empty when all the left parents have been 
        # exhausted but there might exists a right node of the parent
        return self.currentNode is not None or len(self.stack)!=0
    

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