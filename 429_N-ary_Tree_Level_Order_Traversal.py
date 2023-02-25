from typing import List
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        stack=[root]
        answer=[]
        while stack:
            nextStock=[]
            k=[]
            stackLen=len(stack)
            while stackLen>0:
                sr=stack.pop(0)
                stackLen-=1
                if sr:
                # Adding the Values of the Root Node
                    k.append(sr.val)
                    # Adding the children
                    if sr.children:
                        for r in sr.children:
                            nextStock.append(r)
            if k:
                answer.append(k)
            k=[]
            stack=nextStock

        return answer
if __name__=="__main__":
    root=Node(val=1,
              children=[
                            Node(val=3,
                                 children=[
                                            Node(val=5,children=None),
                                            Node(val=6,children=None)
                                            ]),
                            Node(val=2,children=None),
                            Node(val=4,children=None)
              ]
              )
    
    print(Solution().levelOrder(root=root))