# VVI
from typing import Optional,List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        l=0
        r=len(nums)-1
        m=(l+r)//2
        stack=[]
        root=TreeNode(val=nums[m])
        if m-1>=l:
            leftNode=(l,m-1,root,'l')
            stack.append(leftNode)
        if m+1<=r:
            rightNode=(m+1,r,root,'r') 
            stack.append(rightNode)   
        while stack:
            node=stack.pop()
            l,r,parent,side=node
            m=(l+r)//2
            if side=="l":
                parent.left=TreeNode(val=nums[m])
                child=parent.left
            else:
                parent.right=TreeNode(val=nums[m])
                child=parent.right
            if m-1>=l:
                leftNode=(l,m-1,child,'l')
                stack.append(leftNode)
            if m+1<=r:
                rightNode=(m+1,r,child,'r')
                stack.append(rightNode)
        return root


if __name__=="__main__":
    nums=[0,1,2,3,4,5]
    print(Solution().sortedArrayToBST(nums=nums))