class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

b=Node(val=2,children=None)
c=Node(val=3,children=[Node(val=5, children=None),Node(val=6, children=None)])
d=Node(val=4,children=None)
a=Node(val=1,children=[b,c,d])

print(a.children[0].val)


'''
[1,3,6,7]

[2]
'''