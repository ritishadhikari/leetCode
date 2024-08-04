class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count=0
        if root:
            stack=[root]
            tempC={root:[root.val,1]}
            while stack:
                if stack[-1].left is None and stack[-1].right is None:
                    stack.pop()
                    count+=1
                elif (stack[-1].left and stack[-1].left in tempC) or \
                    (stack[-1].right and stack[-1].right in tempC):
                    node=stack.pop()
                    if node.left:
                        tempC[node][0]+=tempC[node.left][0]
                        tempC[node][1]+=tempC[node.left][1]
                    if node.right:
                        tempC[node][0]+=tempC[node.right][0]
                        tempC[node][1]+=tempC[node.right][1]
                    if node.val==tempC[node][0]//tempC[node][1]:
                        count+=1
                else:
                    node=stack[-1]
                    if node.left:
                        stack.append(node.left)
                        tempC[node.left]=[node.left.val,1]
                    if node.right:
                        stack.append(node.right)
                        tempC[node.right]=[node.right.val,1]
        return count



if __name__=="__main__":
    root=TreeNode(val=4,
                    left=TreeNode(val=8,
                                left=TreeNode(val=0,
                                              left=None,
                                              right=None
                                              ),
                                right=TreeNode(val=1,
                                            left=None,
                                            right=None
                                                )
                                    ),
                    right=TreeNode(val=5,
                                   left=None,
                                   right=TreeNode(val=6,
                                                  left=None,
                                                  right=None
                                                  )
                                    )
                            
                    )
    print(Solution().averageOfSubtree(root=root))