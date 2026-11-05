# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #use isSubtree to traverse downwards
        #fail con: reach end of root and dfsMatch is false
        x=False
        if not root and subRoot: return False

        if not subRoot: return True

        if root.val == subRoot.val:
            x = self.dfsMatch(root,subRoot)

        if x ==True:
            return True
        else:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

        
    def dfsMatch(self,root,subRoot):
        if not subRoot and not root: return True
        if not root or not subRoot: return False #we are arriving at null too fast 
        if root.val != subRoot.val:
            return False

        if root.val == subRoot.val:
            return self.dfsMatch(root.left,subRoot.left) and self.dfsMatch(root.right,subRoot.right)
