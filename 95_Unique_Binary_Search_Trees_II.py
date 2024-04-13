from typing import List,Optional
from itertools import permutations
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
     def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        lists=permutations([i for i in range(1,n+1)])

        uniqueTrees=set()
        uniqueArch=set()
        for lst in lists:

            for i,val in enumerate(lst):
                if i==0:
                    tree=TreeNode(val=val)
                    arch={'v':val,'l':{},'r':{}}
                else:
                    realTree=tree
                    realArch=arch
                    while tree:
                        if val<tree.val:
                            if tree.left:
                                tree=tree.left
                                arch=arch['l']
                            else:
                                tree.left=TreeNode(val=val)
                                arch['l']={'v':val,'l':{},'r':{}}
                                break
                        else:
                            if tree.right:
                                tree=tree.right
                                arch=arch['r']
                            else:
                                tree.right=TreeNode(val=val)
                                arch['r']={'v':val,'l':{},'r':{}}
                                break
                    tree=realTree
                    arch=realArch
            if str(arch) not in uniqueArch:
                uniqueArch.add(str(arch))
                uniqueTrees.add(tree)

        return uniqueTrees
     
if __name__=="__main__":
    n=3
    print(Solution().generateTrees(n=3))