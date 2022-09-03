from typing import Optional
from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count=0
        countDict=defaultdict(lambda: [])
        parentDict=defaultdict(lambda : None)
        if root: 
            stack=[root]  
        else:
            stack=[] 
            
        while stack:
            node=stack.pop()
            countDict[node].append(node.val)
            if node.val==targetSum:
                count+=1
            if parentDict[node]:
                for val in countDict[parentDict[node]]:
                    if node.val+val==targetSum:
                        count+=1
                    countDict[node].append(node.val+val)
            if node.left:
                parentDict[node.left]=node
                stack.append(node.left)
            if node.right:
                parentDict[node.right]=node
                stack.append(node.right)
        return count


if __name__=="__main__":
    root=TreeNode(val=5,
                left=TreeNode(val=4,
                            left=TreeNode(val=11,
                                        left=TreeNode(val=7,
                                                    left=None,
                                                    right=None),
                                        right=TreeNode(val=2,
                                                    left=None,
                                                    right=None)),
                            right=None),
                right=TreeNode(val=8,
                            left=TreeNode(val=3,
                                        left=None,
                                        right=None),
                            right=TreeNode(val=4,
                                    left=TreeNode(val=5,
                                                left=None,
                                                right=None),
                                    right=TreeNode(val=1,
                                                left=None,
                                                right=None))))
    targetSum=22                                            
    print(Solution().pathSum(root=root,targetSum=22))