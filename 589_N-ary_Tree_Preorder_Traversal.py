from typing import List
from collections import deque
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        valContainers=[]
        stack=deque([root])
        while stack:
            node=stack.popleft()
            if node:
                valContainers.append(node.val)
                if node.children:
                    stack=deque(node.children+list(stack))
        return valContainers

if __name__=="__main__":
    node=Node(val=1,children=[Node(val=3,children=[Node(val=5,children=None),Node(val=6,children=None)]),Node(val=2,children=None),Node(val=4,children=None)])
    print(Solution().preorder(root=node))